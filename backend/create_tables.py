import asyncio
import sys
from app.db.session import engine
from app.db.models.base import Base
# IMPORTANT: Import models so they are registered with Base
from app.db.models.user import User
from app.db.models.item import Item

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def init_models():
    async with engine.begin() as conn:
        print(">>> Строим таблицы...")
        await conn.run_sync(Base.metadata.drop_all) # Optional: clear old junk
        await conn.run_sync(Base.metadata.create_all)
        print(">>> ГОТОВО! Таблицы users и items созданы.")

if __name__ == "__main__":
    asyncio.run(init_models())