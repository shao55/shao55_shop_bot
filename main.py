import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
import database

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def on_startup():
    await database.create_tables()
    print("Бот запущен!")

async def main():
    # Регистрируем обработчики
    from handlers import user, admin
    user.register_handlers(dp)  
    admin.register_handlers(dp)  # Теперь точно есть эта функция

    # Выполняем действия при старте
    await on_startup()
    
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())