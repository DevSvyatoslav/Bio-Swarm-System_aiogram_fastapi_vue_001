from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from datetime import datetime 

class UserBase(BaseModel):
  username: Optional[str] = None
  # EmailStr - Pydantic сам проверит, что тут есть "@" и "." 
  # Это экономит время: мы не пускаем мусор в базу.
  telegram_id: Optional[int] = None
  is_active: Optional[bool] = True
  is_superuser: bool = False

# --- СХЕМА ДЛЯ СОЗДАНИЯ (Вход) ---
class UserCreate(UserBase):
    email: EmailStr
    password: str 

class UserRead(UserBase):
    id: int
    email: Optional[EmailStr] = None
    created_at: datetime
    model_config = ConfigDict(from_attributes=True) 