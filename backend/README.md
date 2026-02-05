# Bio Swarm System

Telegram Bot + Backend API + Web Dashboard.
Управление роем агентов через Telegram и Веб.

**Tech Stack:**
*   **Python 3.12** (FastAPI, AsyncIO)
*   **PostgreSQL 17** (AsyncPG, SQLAlchemy)
*   **Frontend:** Vue 3 + Vite + Tailwind
*   **Bot:** Aiogram 3

## Setup (Local)

Проект оптимизирован под Windows/Linux.

### 1. Backend
```bash
cd backend
python -m venv venv
# Win:
venv\Scripts\activate

pip install -r requirements.txt
# Create .env file first!
alembic upgrade head

# Start
uvicorn app.server:app --reload --port 8001