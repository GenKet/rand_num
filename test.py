from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.state import State,StatesGroup
import random


TOKEN = "6678883418:AAE0QtMGuG-D11mHiKwDmdqU0-d_PWF8MrM"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(Command("start"))
async def start_on(message: types.Message):
    await bot.send_message(message.chat.id,"Угадай число от 1 до 10")

@dp.message_handler()
async def random_num(message: types.Message):
    number = random.randint(1, 10)
    if message.text.isdigit():
        if int(message.text) == number:
            await bot.send_message(message.chat.id,"Вы угадали")
        else:
            await bot.send_message(message.chat.id, f"Вы не угадали, я загадал {number}")
    else:
        await bot.send_message(message.chat.id, "Введи корректное число")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

