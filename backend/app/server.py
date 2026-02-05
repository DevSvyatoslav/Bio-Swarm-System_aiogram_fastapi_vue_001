from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router # <--- ЭТОТ ИМПОРТ ВАЖЕН

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Swarm Core Systems: ONLINE")
    yield
    print("💤 Swarm Core Systems: SHUTDOWN")

app = FastAPI(
    title="Digital Swarm AGI",
    version="0.1.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Разрешаем ВСЕМ
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check
@app.get("/system/health")
async def health_check():
    return {
        "status": "operational",
        "system": "Bio Swarm Node"
    }

# ПОДКЛЮЧЕНИЕ РОУТОВ (Вот здесь подключаются Users)
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Swarm Node Active"}