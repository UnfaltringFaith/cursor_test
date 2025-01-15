from aiogram import Bot, Dispatcher, types, F, Router, html
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, LinkPreviewOptions
from aiogram.enums import ParseMode
from aiogram.utils.formatting import (Bold, as_list, as_marked_section, as_key_value, HashTag) 
import logging
import asyncio
from datetime import datetime

import re

import app.keyboards as kb

router = Router()

#Включение базового логирования
logging.basicConfig(level=logging.INFO)
@router.message(CommandStart(deep_link=True, magic=F.args.regexp(re.compile(r'book_(\d+)'))))
async def cmd_start(message: Message, command: CommandObject):
    book_number = command.args.split('_')[1]
    await message.reply(f'Informaion about book №{book_number} ')

@router.message(Command('help'))
@router.message(CommandStart(deep_link=True, magic=F.args == 'help'))
async def start1(message: Message):
    await message.answer(f'Привет, {html.spoiler(html.quote(message.from_user.full_name))}, какая помошь необходима?', reply_markup=kb.setting)

@router.message(F.text == 'Как дела?')
async def deal_react(message: Message):
    await message.answer(f'Все хорошо, а у <i>тебя</i>?')

@router.message(F.text == "Артисты")
async def show_artists(message: Message):
    await message.answer("Популярные артисты",reply_markup= await kb.inline_cars())

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID photo: {message.photo[-1].file_id}")

@router.message(Command("get_information"))
async def get_information(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! {"Ты премиум пользователь Telegram!"  if message.from_user.is_premium else "Ты не премиум пользователь Telegram!"} \nТвой тег: {message.from_user.username}.")

#Бросок кубика
@router.message(lambda comm: comm.text.lower() == 'dice')
async def some_text(msg: Message):
    dice_result = await msg.answer_dice(emoji="🎲")

    dice_value = dice_result.dice.value
    await asyncio.sleep(5)

    await msg.answer(f'Вам выпало {dice_value}')

@router.message(Command("start_time"))
async def start_time(msg: Message, started_at: str):
    await msg.answer(f"Bot start usage time: {started_at}")

@router.message(Command("add_to_list"))
async def start_time(msg: Message, my_list: list[int]):
    my_list.append(4)
    await msg.answer(f"List size: {len(my_list)}")

@router.message(Command("msg"))
async def msg_func(msg: Message):
    await msg.answer(f"Message:")

@router.message(Command("settimer", prefix="!"))
async def set_timer(msg: Message, command: CommandObject):
    if command.args is None:
        await msg.answer("Please provide a time in seconds")
        return
    try:
        timer_time, command_text = (command.args).split(' ', maxsplit=1)
    except ValueError:
        await msg.answer("Please provide a time in seconds")
        return

    await msg.answer(f"Timer set for {timer_time} seconds")


@router.message(Command("links"))
async def links(msg: Message):
    links = (
        "https://www.google.com"
        "\n"
        "https://www.youtube.com"
    )

    options_1 = LinkPreviewOptions(
        is_disabled=True
    )

    await msg.answer(f"There's no preview for {links}", link_preview_options=options_1)

    options_2 = LinkPreviewOptions(
        prefer_small_media=True,
        url = "https://www.youtube.com"
    )

    await msg.answer(f"There's no preview for {links}", link_preview_options=options_2)

@router.message(F.text)
async def msg_func(msg: Message):

    time_now = datetime.now().strftime("%H:%M")
    tag_text = f"Created at: {time_now}"
    await msg.answer(f"{msg.html_text}\n\n{html.underline(tag_text)}")
