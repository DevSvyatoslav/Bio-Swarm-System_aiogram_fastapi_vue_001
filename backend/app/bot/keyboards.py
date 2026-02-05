from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# main menu for user
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👤 Профиль"), KeyboardButton(text="📊 Статус Системы")],
        [KeyboardButton(text="🔗 Привязать Email")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие..."
)