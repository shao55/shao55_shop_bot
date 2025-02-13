from aiogram import Router, types
from aiogram.filters import Command

# Создаём роутер
router = Router()

# Обработчик команды /admin
@router.message(Command("admin"))
async def admin_panel(message: types.Message):
    await message.answer("Добро пожаловать в панель администратора!")

# Функция для регистрации обработчиков
def register_handlers(dp):
    dp.include_router(router)
