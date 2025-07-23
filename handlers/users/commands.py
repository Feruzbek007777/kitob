from telebot.types import Message
from data.loader import bot

from keyboards.inline import books

@bot.message_handler(commands=["start"])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    text = (f"Assalomu alaykum {full_name} tugmani bosing ! ")
    bot.send_message(chat_id, text,
                     reply_markup=books())
