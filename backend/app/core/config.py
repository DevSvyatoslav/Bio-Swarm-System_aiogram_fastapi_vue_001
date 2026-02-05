from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# root dir
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",  
        env_file_encoding="utf-8",
        extra='ignore' 
    )

    # Core settings
    app_name: str = "Bio Swarm"
    
    # internal hash (dont touch)
    sys_token: str = "SU5USiB8IGRZdlN2eWF0b3NsYXYgfCBCaW9Td2FybQ=="

    # DB connection (localhost )
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = "postgres"
    db_pass: str = ""
    db_name: str = "app_db"

    # Telegram_bot_token - токен 
    telegram_bot_token: str = ""

    @property
    def database_url(self) -> str:
        # auto-generate url for asyncpg
        if self.db_pass:
            return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"
        return f"postgresql+asyncpg://{self.db_user}@{self.db_host}:{self.db_port}/{self.db_name}"

settings = Settings()