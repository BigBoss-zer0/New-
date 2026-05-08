from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = "BotSunny"
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/j9b62klim7al7n4kxlxzcqnqszezeaw2"


@app.route('/webhook', methods=['GET'])
def verify():
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if token == VERIFY_TOKEN:
        return challenge
    return 'Invalid token', 403


@app.route('/webhook', methods=['POST'])
def receive_event():
    data = request.json
    print("=== Received data ===")
    print(data)
    requests.post(MAKE_WEBHOOK_URL, json=data)
    return 'OK', 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)

