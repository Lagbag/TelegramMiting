from telegram import Update  # Импорт класса Update для работы с обновлениями
from telegram.ext import Application, CommandHandler, \
    ContextTypes  # Импорт нужных классов для работы с хендлерами и ботом

# Токен вашего бота, полученный от BotFather в Telegram
TOKEN = '7416329393:AAHRpe8d5Z4K6IBd_KnajGy-nbi7ELWZX1M'


# Асинхронная функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Обрабатывает команду /start и отправляет приветственное сообщение пользователю.

    Args:
        update (Update): Объект, содержащий информацию о текущем обновлении.
        context (ContextTypes.DEFAULT_TYPE): Объект контекста, содержащий данные и методы для обработки запроса.
    """
    # Отправка приветственного сообщения
    await update.message.reply_text("Hello, World! Добро пожаловать в нашего бота!")


# Функция main для настройки и запуска бота
def main() -> None:
    """
    Основная функция, инициализирующая и запускающая бота.
    """
    # Создание объекта приложения (бота) с токеном
    application = Application.builder().token(TOKEN).build()

    # Создание обработчика для команды /start и добавление его в приложение
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    # Запуск бота и ожидание обновлений
    application.run_polling()


# Запуск основной функции, если скрипт запускается напрямую
if __name__ == "__main__":
    main()
