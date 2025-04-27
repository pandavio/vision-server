from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import io
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# 初始化模型（只加载一次）
print("🚀 正在加载图像识别模型...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
print("✅ 模型加载完成")

app = Flask(__name__)
CORS(app)

# 可用作健康检查（浏览器访问 https://xxx.onrender.com/ping）
@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({"error": "Missing image"}), 400

        print("📥 收到图片请求，正在分析...")

        # 解码 base64 图像
        image_data = base64.b64decode(data['image'])
        image = Image.open(io.BytesIO(image_data)).convert("RGB")

        # 图像描述生成
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)

        print("✅ 分析完成，描述：", caption)

        return jsonify({"description": caption})
    except Exception as e:
        print("❌ 处理失败:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    print(f"🌍 正在监听端口 {port} ...")
    app.run(host="0.0.0.0", port=port)
