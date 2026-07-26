import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]


def send_message(message):
    """
    Send a message to Telegram.
    """

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "disable_web_page_preview": True
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("✅ Telegram message sent.")
    else:
        print("❌ Telegram Error")
        print(response.text)
