from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def books():
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("📖 Kitoblar", callback_data="turlari")
    btn2 = InlineKeyboardButton("🖊 Avtorlar", callback_data="avtorlar")
    btn3 = InlineKeyboardButton("📚 Asarlar", callback_data="asarlar")
    markup.add(btn1, btn2, btn3)
    return markup