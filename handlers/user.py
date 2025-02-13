from aiogram import Router, types
from aiogram.filters import Command
from database import get_categories
from keyboards import main_menu, categories_kb

# Создаём роутер
router = Router()

# Обработка команды /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот для заказов.\nВыбери действие:",
        reply_markup=main_menu()
    )

# Показ категорий
@router.message(Command("categories"))
async def show_categories(message: types.Message):
    categories = await get_categories()
    await message.answer(
        "Выберите категорию:",
        reply_markup=categories_kb(categories)
    )

# Обработка нажатий кнопок "Меню", "Корзина" и "Помощь"
@router.message(lambda message: message.text == "🍔 Меню")
async def menu(message: types.Message):
    await message.answer("Вы выбрали Меню.")

@router.message(lambda message: message.text == "🛒 Корзина")
async def cart(message: types.Message):
    await message.answer("Вы выбрали Корзину.")

@router.message(lambda message: message.text == "🆘 Помощь")
async def help(message: types.Message):
    await message.answer("Вы выбрали Помощь.")

# Функция для регистрации обработчиков
def register_handlers(dp):
    dp.include_router(router)