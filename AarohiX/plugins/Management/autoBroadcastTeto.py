import asyncio
import datetime
from AarohiX import app
from pyrogram import Client
from AarohiX.utils.database import get_served_chats
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_IMG_URL = "https://telegra.ph/file/0677e881a84925cb9c789.jpg"


MESSAGE = f"""◍ بوت ميوزك لتشغيل الاغاني بالمجموعات والقنوات الاسرع من باقي البوتات 💌

اوامر تسليه بالبوت و الحمايه من الاسبام ❄

- يدعم خاصيه تفعيل الاذان و المزيد من المميزات التي لا حصر لها

➲ المعـرف : @{app.username}
"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ضيفني لمجموعتك ❄", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)
                except Exception as e:
                    pass  
    except Exception as e:
        pass  

async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(70000)  
        
asyncio.create_task(continuous_broadcast())
