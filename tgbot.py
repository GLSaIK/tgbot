import nest_asyncio
import os
nest_asyncio.apply()
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
import pytz
MSK = pytz.timezone("Europe/Moscow")
# Указываем дату начала лета (1 июня текущего года)
def get_seconds_since_summer_start():
    now = datetime.now(MSK)
    summer_start = MSK.localize(datetime(now.year, 6, 1))
    delta = now - summer_start
    seconds = int(delta.total_seconds())
    min = (seconds // 60)
    return seconds, min

# Обработчик команды /start или /seconds
async def seconds_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    seconds, min = get_seconds_since_summer_start()
    if seconds < 0:
        await update.message.reply_text("лето еще не начилось, терпи")
    elif seconds > 7948800:
        await update.message.reply_text("лето уже кончилось")
    else:
        await update.message.reply_text(f"прошло {seconds} секунд или {min} минут лета")

async def startcom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    seconds, min = get_seconds_since_summer_start()
    if seconds < 0:
        await update.message.reply_text("вот ты старт жмешь, а лета еще нет")
    elif seconds > 7948800:
        await update.message.reply_text("вот ты старт жмешь, а лето уже кончилось")
    else:
        await update.message.reply_text(f"вот ты старт жмешь, а прошло уже {seconds} секунд или {min} минут лета")

# Основная функция запуска бота
async def main():
    # Замени 'YOUR_TOKEN_HERE' на токен, выданный BotFather
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN).build()

    # Добавляем команду
    app.add_handler(CommandHandler("start", startcom))
    app.add_handler(CommandHandler("time", seconds_command))

    print("Бот запущен!")
    await app.run_polling()

# Запуск бота
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


