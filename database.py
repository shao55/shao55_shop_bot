import asyncpg
from config import DATABASE_URL

# Подключение к БД
async def create_tables():
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.close()

# Получение категорий
async def get_categories():
    conn = await asyncpg.connect(DATABASE_URL)
    categories = await conn.fetch("SELECT * FROM categories")
    await conn.close()
    return categories