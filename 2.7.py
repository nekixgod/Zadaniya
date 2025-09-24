from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '8229577510:AAGOAEhbjYG5EPnua1ERftH9MATGrxdeaOY'


# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


buttons: list[KeyboardButton] = []
keyboard: list[list[KeyboardButton]] = []


# Заполняем список списками с кнопками
for i in range(1, 1201):
    buttons.append(KeyboardButton(text=str(i)))
    if not i % 12:
        keyboard.append(buttons)
        buttons = []
        keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=f'Кнопка {i}')] for i in range(1, 351)]



# Создаем объект клавиатуры, добавляя в него список списков с кнопками
keyboard = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)









# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Чего кошки боятся больше?',
        reply_markup=keyboard
    )




# Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
@dp.message(F.text == 'Собак 🦮')
async def process_dog_answer(message: Message):
    await message.answer(
        text='Да, несомненно, кошки боятся собак. '
             'Но вы видели как они боятся огурцов?'
    )




# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
@dp.message(F.text == 'Огурцов 🥒')
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='Да, иногда кажется, что огурцов '
             'кошки боятся больше'
    )





if __name__ == '__main__':
    dp.run_polling(bot)
