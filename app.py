from flask import Flask, request
import requests
from datetime import datetime, timezone, timedelta
app = Flask(name)
VERIFY_TOKEN = "BotSunny"
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/j9b62klim7al7n4kxlxzcqnqszezeaw2"  # ← ใส่ URL จาก Make
THAI_TZ = timezone(timedelta(hours=7))
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
    # ส่งต่อไป Make โดยตรง
    requests.post(MAKE_WEBHOOK_URL, json=data)
    return 'OK', 200
if name == 'main':
    app.run(port=5000, debug=True)
