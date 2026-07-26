import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

message = """✅ Kolkata Hiring Alerts Started Successfully!

GitHub Actions is working correctly.

Next step: LinkedIn Hiring Search 🚀
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print("Message sent successfully.")
