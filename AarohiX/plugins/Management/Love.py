from pyrogram import Client, filters
import random
from AarohiX import app

def احصل_على_رسالة_عشوائية(نسبة_الحب):
    if نسبة_الحب <= 30:
        return random.choice([
            "الحب في الهواء لكنه يحتاج إلى شرارة صغيرة.",
            "بداية جيدة لكن هناك مجال للنمو.",
            "إنها مجرد بداية لشيء جميل."
        ])
    elif نسبة_الحب <= 70:
        return random.choice([
            "هناك اتصال قوي. استمر في تنميته.",
            "لديك فرصة جيدة. اعمل عليها.",
            "الحب يتفتح، استمر في السير على هذا الطريق."
        ])
    else:
        return random.choice([
            "واو! إنها مباراة مصنوعة في الجنة!",
            "مباراة مثالية! احتفظ بهذه العلاقة.",
            "مقدر لكما أن تكونا معًا. تهانينا!"
        ])
        
@app.on_message(filters.command("الحب", prefixes="/"))
def أمر_الحب(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        اسم1 = args[0].strip()
        اسم2 = args[1].strip()
        
        نسبة_الحب = random.randint(10, 100)
        رسالة_الحب = احصل_على_رسالة_عشوائية(نسبة_الحب)

        الرد = f"{اسم1}💕 + {اسم2}💕 = {نسبة_الحب}%\n\n{رسالة_الحب}"
    else:
        الرد = "يرجى إدخال اسمين بعد أمر /الحب."
    app.send_message(message.chat.id, الرد)
