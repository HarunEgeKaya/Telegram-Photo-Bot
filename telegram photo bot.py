from telebot import TeleBot
from telebot.types import Message
import requests

bot = TeleBot("!Your Token!")

@bot.message_handler(content_types=['photo'])
def handle_photo(message: Message):
    photo_id = message.photo[-1].file_id
    file_info = bot.get_file(photo_id)
    file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"
    
    bot.send_message(message.chat.id, f"Fotoğraf URL'si: {file_url}")

bot.infinity_polling()
