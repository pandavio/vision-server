from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import openai
import os

# 初始化
print("🚀 正在初始化 OpenAI 视觉问答服务器...")

client = openai.OpenAI(api_key="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")  # ✅换成你的

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

        print("📥 收到图像 + 问题请求")

        # base64数据
        base64_image = data['image']

        # 用户问题
        question = data['question']
        print(f"🗣️ 用户问题: {question}")

        # 判断语言
        is_chinese = any('\u4e00' <= c <= '\u9fff' for c in question)
        system_prompt = "请用中文回答。" if is_chinese else "Please answer in English."
        print(f"🌐 自动选择回答语言提示: {system_prompt}")

        # 调用 GPT-4o，直接用 Base64的 inline image_url
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
        print(f"🤖 GPT回答: {final_answer}")

        return jsonify({
            "question": question,
            "answer": final_answer
        })

    except Exception as e:
        print("❌ 错误:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 正在监听端口 {port}")
    app.run(host="0.0.0.0", port=port)

