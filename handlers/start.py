from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.inline_keyboard_button import InlineKeyboardButton as IButton
<<<<<<< HEAD
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
=======
from  aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
>>>>>>> 2020f770811ad87bd7893a1ada5f3101a482d855
import random
import os

start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [IButton(text="Наш сайт", url="https://google.com"),
<<<<<<< HEAD
             IButton(text="Наш инстограмм", url="https://instagram.com"),
=======
             IButton(text="Наш сайт", url="https://instagram.com"),
>>>>>>> 2020f770811ad87bd7893a1ada5f3101a482d855
            ],
            [
                IButton(text="О нас", callback_data="about")
            ]
        ]
    )
    await message.answer("Привет, друзья", reply_markup=kb)

@start_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
<<<<<<< HEAD
    await callback.answer()
=======
    await  callback.answer()
>>>>>>> 2020f770811ad87bd7893a1ada5f3101a482d855
    await callback.message.answer("О нас")

@start_router.message(Command("photo"))
async def send_random_picture(message: types.Message):
    images_folder = "images/"
    images = [f for f in os.listdir(images_folder) if f.endswith((".jpg", ".jpeg", ".png"))]

    if images:
        random_image = random.choice(images)
        file = types.FSInputFile(images_folder + random_image)
        await message.answer_photo(file)
    else:
        await message.answer("В папке с картинками нет подходящих файлов.")


@start_router.message(Command("myinfo"))
async def my_info(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username

    info_message = f"Ваш ID: {user_id}\nИмя: {first_name}\nUsername: @{username}"
    await message.answer(info_message)
