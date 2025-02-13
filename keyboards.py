from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню
def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🍔 Меню"), KeyboardButton(text="🛒 Корзина")],
            [KeyboardButton(text="🆘 Помощь")]
        ],
        resize_keyboard=True
    )

# Кнопки для категорий
def categories_kb(categories):
    keyboard = InlineKeyboardMarkup()
    for category in categories:
        keyboard.add(InlineKeyboardButton(
            text=category['name'],
            callback_data=f"cat_{category['id']}"
        ))
    return keyboard