from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import io
from PIL import Image
from transformers import BlipProcessor, Blip2ForConditionalGeneration  # ✅ 用 BLIP-2 正确类
import torch

# 初始化图像问答模型
print("🚀 正在加载 BLIP-2 图像问答模型...")
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 加载模型和处理器（注意模型类必须是 Blip2ForConditionalGeneration）
processor = BlipProcessor.from_pretrained("Salesforce/blip2-flan-t5-xl")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-flan-t5-xl").to(device)
print("✅ BLIP-2 模型加载完成")

# 初始化 Flask 应用
app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False  # 确保返回的 JSON 中文不乱码

@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        if not data or 'image' not in data or 'question' not in data:
            return jsonify({"error": "Missing image or question"}), 400

        print("📥 收到图像 + 问题请求")

        # 解码图像
        image_data = base64.b64decode(data['image'])
        image = Image.open(io.BytesIO(image_data)).convert("RGB")

        # 处理用户提问
        question = data['question']
        print(f"🗣️ 用户问题: {question}")

        # 推理：图像 + 问题
        inputs = processor(image, text=question, return_tensors="pt").to(device)
        out = model.generate(**inputs)
        answer = processor.decode(out[0], skip_special_tokens=True)

        print(f"🤖 模型回答: {answer}")

        return jsonify({
            "question": question,
            "answer": answer
        })

    except Exception as e:
        print("❌ 错误:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 正在监听端口 {port}")
    app.run(host="0.0.0.0", port=port)
