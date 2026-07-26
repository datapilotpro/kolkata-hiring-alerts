import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

message = """✅ Kolkata Hiring Alerts Started Successfully!

GitHub Actions is working correctly.

Next step: LinkedIn Hiring Search 🚀
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print("Status Code:", response.status_code)
print("Response:", response.text)
print("Message sent successfully.")
