from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域访问

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    if not data or 'image' not in data:
        return jsonify({"error": "Missing image"}), 400

    # 模拟图像识别返回内容
    return jsonify({
        "description": "前方 3 米为斑马线，右侧是红绿灯路口。"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
