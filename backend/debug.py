import asyncio
import asyncpg
import sys
import os
from dotenv import load_dotenv

# --- ЛЕКАРСТВО ОТ WINDOWS ---
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def test_connection():
    # Загружаем настройки из .env
    load_dotenv()
    
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASS", "swarm_admin_2024")
    host = os.getenv("DB_HOST", "127.0.0.1")
    dbname = os.getenv("DB_NAME", "app_db")
    
    print(f"1. Проверяем настройки: User={user}, Host={host}, DB={dbname}")
    
    dsn = f"postgresql://{user}:{password}@{host}:5432/{dbname}"
    
    print("2. Попытка подключения...")
    try:
        conn = await asyncpg.connect(dsn)
        print("✅ УСПЕХ! БАЗА ДАННЫХ ОТВЕЧАЕТ.")
        await conn.close()
    except Exception as e:
        print("❌ ОШИБКА ПОДКЛЮЧЕНИЯ!")
        print(e)

if __name__ == "__main__":
    asyncio.run(test_connection())