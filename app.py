from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import openai
import os

import torch
from PIL import Image
from io import BytesIO

print("🚀 正在初始化 OpenAI + YOLO 视觉服务器...")

# OpenAI 初始化
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# YOLOv5 加载（本地模型）
print("🔍 正在加载 YOLOv5 本地模型...")
yolo_model = torch.hub.load(
    repo_or_dir='yolov5',
    model='custom',
    path='yolov5/models/yolov5s.pt',
    source='local'
)
yolo_model.eval()

# YOLO 检测函数
def run_yolo_detection(base64_img):
    try:
        image_data = base64.b64decode(base64_img)
        image = Image.open(BytesIO(image_data)).convert("RGB")
        results = yolo_model(image)
        labels = results.pandas().xyxy[0]['name'].tolist()
        print(f"🟢 YOLO 识别到: {labels}")
        return labels
    except Exception as e:
        print("❌ YOLO识别失败:", e)
        return []

# Flask 初始化
app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json(force=True)
        if not data or 'image' not in data or 'question' not in data:
            return jsonify({"error": "Missing image or question"}), 400

        base64_image = data['image']
        question = data['question']
        system_prompt = data.get('system_prompt', '')  # 👈 支持前端传来的提示词

        print("📥 收到请求，问题:", question)

        # 判断是否 YOLO 模式
        if any(k in question.lower() for k in ["识别", "detect", "检测", "看到了什么", "看到什么", "有什么"]):
            labels = run_yolo_detection(base64_image)
            return jsonify({
                "question": question,
                "mode": "yolo",
                "answer": "识别到物体：" + (", ".join(labels) if labels else "未检测到物体"),
                "labels": labels
            })

        # 使用前端传来的 system_prompt，否则按语言自动判断
        if not system_prompt:
            is_chinese = any('\u4e00' <= c <= '\u9fff' for c in question)
            system_prompt = "请用中文回答。" if is_chinese else "Please answer in English."
        print(f"🌐 使用 GPT-4o，系统提示: {system_prompt}")

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": [
                    {"type": "text", "text": question},
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }}
                ]}
            ],
            max_tokens=1000
        )

        final_answer = response.choices[0].message.content.strip()
        print(f"🤖 GPT 回答: {final_answer}")

        return jsonify({
            "question": question,
            "mode": "gpt4o",
            "answer": final_answer
        })

    except Exception as e:
        print("❌ 发生错误:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 正在监听端口 {port}")
    app.run(host="0.0.0.0", port=port)
