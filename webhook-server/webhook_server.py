from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receive_alert():
    data = request.get_json()
    
    print("\n📢 [Webhook Alert Received] 📢")
    print(f"🔹 Client IP: {request.remote_addr}")  # 요청 보낸 클라이언트 IP
    print(f"🔹 Headers:\n{request.headers}")  # 모든 요청 헤더 출력
    print(f"🔹 Body:\n{data}")  # JSON 데이터 출력

    if not data:
        return jsonify({"error": "No data received"}), 400  # 데이터가 없으면 오류 반환
    
    return jsonify({"status": "success", "received_data": data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
