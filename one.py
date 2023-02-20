import telebot
import mysql.connector

bot = telebot.TeleBot("6262622771:AAEbHR-8RlopH8O0OPx0dN6iO0JRt-gk7G0")
conn = mysql.connector.connect(
    host="mysql.j98515082.myjino.ru",
    user="j98515082",
    password="HiuhasUH83",
    database="j98515082_test"
)

@bot.message_handler(func=lambda message: True)
def save_message(message):
    user_id = message.from_user.id
    text = message.text
    created_at = message.date
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (user_id, message, created_at) VALUES (%s, %s, %s)", (user_id, text, created_at))
    conn.commit()
    bot.reply_to(message, "Сообщение успешно сохранено в базу данных!")

bot.polling()
