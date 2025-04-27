from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import io
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration, pipeline

# 初始化图像描述模型
print("🚀 正在加载图像识别模型...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
print("✅ 图像模型加载完成")

# 初始化翻译模型（英文 → 中文）
print("🌐 正在加载翻译模型...")
translator = pipeline("translation_en_to_zh", model="Helsinki-NLP/opus-mt-en-zh")
print("✅ 翻译模型加载完成")

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({"error": "Missing image"}), 400

        print("📥 收到图像上传请求...")

        image_data = base64.b64decode(data['image'])
        image = Image.open(io.BytesIO(image_data)).convert("RGB")

        # 图像描述生成（英文）
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs)
        caption_en = processor.decode(out[0], skip_special_tokens=True)

        # 翻译为中文
        translation = translator(caption_en, max_length=100)
        caption_zh = translation[0]["translation_text"]

        print(f"🔎 英文: {caption_en}")
        print(f"🇨🇳 中文: {caption_zh}")

        return jsonify({
            "description_en": caption_en,
            "description_zh": caption_zh
        })

    except Exception as e:
        print("❌ 错误:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 正在监听端口 {port}")
    app.run(host="0.0.0.0", port=port)
