import os
import time
import requests
import json

TOKEN = os.environ.get("RUBIKA_BOT_TOKEN")

if not TOKEN:
    print("❌ توکن پیدا نشد!")
    exit(1)

print("✅ توکن پیدا شد. در حال اتصال به روبیکا...")

# آدرس API روبیکا
BASE_URL = f"https://api.robika.ir/bot{TOKEN}/"

def get_updates(offset=None):
    url = BASE_URL + "getUpdates"
    params = {"timeout": 30}
    if offset:
        params["offset"] = offset
    try:
        res = requests.get(url, params=params, timeout=35)
        if res.status_code == 200:
            return res.json().get("result", [])
    except Exception as e:
        print(f"خطا در اتصال: {e}")
    return []

def send_message(chat_id, text):
    url = BASE_URL + "sendMessage"
    data = {"chat_id": chat_id, "text": text}
    try:
        requests.post(url, data=data, timeout=10)
    except Exception as e:
        print(f"خطا در ارسال: {e}")

print("🚀 ربات روشن شد و منتظر پیامه...")

last_update_id = 0

while True:
    updates = get_updates(offset=last_update_id + 1)
    for update in updates:
        last_update_id = update.get("update_id", last_update_id)
        message = update.get("message")
        
        if message and "text" in message:
            chat_id = message["chat"]["id"]
            text = message["text"]
            
            if text == "سلام":
                send_message(chat_id, "سلام داداش! ربات بدون کتابخانه وصله ⚡")
                print(f"پیام 'سلام' از {chat_id} دریافت و پاسخ داده شد.")
    
    time.sleep(1) # یه ثانیه صبر میکنه تا سرور روبیکا اذیت نشه
