from telegram import Update  # Импорт класса Update для работы с обновлениями
from telegram.ext import Application, MessageHandler, filters, \
    ContextTypes  # Импорт классов для работы с хендлерами и фильтрами

# Токен вашего бота, полученный от BotFather в Telegram
TOKEN = '7416329393:AAHRpe8d5Z4K6IBd_KnajGy-nbi7ELWZX1M'


# Асинхронная функция для обработки текстовых сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Обрабатывает любое текстовое сообщение и отправляет его обратно пользователю.

    Args:
        update (Update): Объект, содержащий информацию о текущем обновлении.
        context (ContextTypes.DEFAULT_TYPE): Объект контекста, содержащий данные и методы для обработки запроса.
    """
    # Получение текста сообщения от пользователя
    user_message = update.message.text

    # Отправка эхо-ответа с тем же текстом
    await update.message.reply_text(user_message)


# Основная функция для настройки и запуска бота
def main() -> None:
    """
    Основная функция, инициализирующая и запускающая бота.
    """
    # Создание объекта приложения (бота) с токеном
    application = Application.builder().token(TOKEN).build()

    # Создание обработчика сообщений, который реагирует на все текстовые сообщения
    echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(echo_handler)

    # Запуск бота и ожидание новых сообщений
    application.run_polling()


# Запуск основной функции, если скрипт запускается напрямую
if __name__ == "__main__":
    main()
