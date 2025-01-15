from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Артисты")],
    [KeyboardButton(text="Корзина"), KeyboardButton(text="Баланс")]
],resize_keyboard=True, input_field_placeholder="Выберите пункт меню")

setting = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Обо мне", url="https://dzen.ru/?yredirect=true")],
])

artists = {"the weeknd": "https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ?si=duS_fC7LQeqsZkzw1tVNHg", "Adele": "https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY?si=VS6uwoGVQ46zbWzHx_GjnA", "joji": "https://open.spotify.com/artist/3MZsBdqDrRTJihTHQrO6Dq?si=kT9zMYMuTYWX6qCp038vVw"}

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for artist, url1 in artists.items():
        keyboard.add(InlineKeyboardButton(text=artist, url=url1))

    return keyboard.adjust(3).as_markup()