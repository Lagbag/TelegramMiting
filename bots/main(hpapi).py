import requests
import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Замените на ваш токен
API_TOKEN = '7416329393:AAHRpe8d5Z4K6IBd_KnajGy-nbi7ELWZX1M'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

BASE_URL = "http://localhost:5000/api"

# Команда /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для получения информации о персонажах и заклинаниях. Вот, что я умею:\n\n"
                        "/characters - Случайные персонажи\n"
                        "/students - Случайные студенты\n"
                        "/staff - Случайные сотрудники\n"
                        "/house_gryffindor - Случайные персонажи из Гриффиндора\n"
                        "/spells - Случайные заклинания")

# Общая функция для случайного выбора
async def send_random_selection(message, endpoint, item_name):
    response = requests.get(f"{BASE_URL}/{endpoint}")
    if response.status_code == 200:
        items = response.json()
        random_items = random.sample(items, min(5, len(items)))  # Выбор случайных 3-5 записей
        for item in random_items:
            name = item.get("name", "Безымянный")
            description = item.get("description", "Описание отсутствует")
            image_url = item.get("image_url")  # Предполагается, что API возвращает URL изображения

            # Отправка с изображением, если оно доступно
            if image_url:
                await bot.send_photo(chat_id=message.chat.id, photo=image_url,
                                     caption=f"{name}\n\n{description}")
            else:
                await message.reply(f"{name}\n\n{description}")
    else:
        await message.reply("Ошибка при получении данных.")

# Команда для случайных персонажей
@dp.message_handler(commands=['characters'])
async def get_random_characters(message: types.Message):
    await send_random_selection(message, "characters", "Персонажи")

# Команда для случайных студентов
@dp.message_handler(commands=['students'])
async def get_random_students(message: types.Message):
    await send_random_selection(message, "characters/students", "Студенты")

# Команда для случайных сотрудников
@dp.message_handler(commands=['staff'])
async def get_random_staff(message: types.Message):
    await send_random_selection(message, "characters/staff", "Сотрудники")

# Команда для случайных персонажей из Гриффиндора
@dp.message_handler(commands=['house_gryffindor'])
async def get_random_gryffindor_characters(message: types.Message):
    await send_random_selection(message, "characters/house/Gryffindor", "Гриффиндорцы")

# Команда для случайных заклинаний
@dp.message_handler(commands=['spells'])
async def get_random_spells(message: types.Message):
    await send_random_selection(message, "spells", "Заклинания")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
