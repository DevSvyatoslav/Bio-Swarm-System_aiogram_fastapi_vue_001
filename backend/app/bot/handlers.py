from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from sqlalchemy import select

from app.db.session import AsyncSessionLocal
from app.db.models.user import User
from app.bot.keyboards import main_keyboard

router = Router()

@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}!\n"
        "Я бот системы Bio Swarm. Я умею работать с твоей базой данных.",
        reply_markup=main_keyboard
    )

@router.message(F.text == "📊 Статус Системы")
async def system_status(message: types.Message):
    # just fake status check
    await message.answer("🟢 System: ONLINE\n🟢 Database: CONNECTED\n🚀 Speed: 100%")

@router.message(F.text == "🔗 Привязать Email")
async def connect_instruction(message: types.Message):
    await message.answer(
        "Чтобы связать аккаунт, напиши команду:\n"
        "`/connect твой_email@gmail.com`",
        parse_mode="Markdown"
    )

@router.message(Command("connect"))
async def connect_account(message: types.Message):
    # parsing email from message
    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("⚠️ Ты забыл написать email.\nПример: /connect neo@matrix.com")
        return
    
    email = parts[1]

    async with AsyncSessionLocal() as session:
        # check if user exists
        result = await session.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()

        if not user:
            await message.answer("❌ Такой email не найден в базе. Сначала зарегайся на сайте!")
            return
        
        # update telegram id
        user.telegram_id = message.from_user.id
        await session.commit()
        
        await message.answer(f"✅ Успех! Аккаунт {user.username} привязан.")

@router.message(F.text == "👤 Профиль")
async def get_profile(message: types.Message):
    async with AsyncSessionLocal() as session:
        # find user by tg id
        query = select(User).where(User.telegram_id == message.from_user.id)
        result = await session.execute(query)
        user = result.scalar_one_or_none()

        if not user:
            await message.answer("Я тебя не знаю 🤷‍♂️\nНажми 'Привязать Email'")
            return

        role = "Админ 👑" if user.is_superuser else "Пользователь 👤"
        
        await message.answer(
            f"📂 **ТВОЙ ПРОФИЛЬ**\n"
            f"ID: {user.id}\n"
            f"Ник: {user.username}\n"
            f"Email: {user.email}\n"
            f"Роль: {role}",
            parse_mode="Markdown"
        )