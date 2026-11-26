
import os
import requests
from datetime import datetime, timezone

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def send_report():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    message = (
        "🤖 SETHA MONITOR\n\n"
        "✅ Bot berhasil dijalankan!\n"
        "📸 Instagram: @rr.setha\n"
        "🎵 TikTok: @s.setha8\n"
        "🎵 TikTok: @rrs_196\n\n"
        f"🕒 Waktu pemeriksaan: {now}\n\n"
        "Monitoring data belum diaktifkan."
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={"chat_id": CHAT_ID, "text": message},
        timeout=20
    )
    response.raise_for_status()
    print("Telegram report sent successfully")

if __name__ == "__main__":
    send_report()
