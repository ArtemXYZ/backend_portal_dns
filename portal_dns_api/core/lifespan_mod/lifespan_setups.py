"""
    Модуль содержит настройки выполнения программ до запуска и после их запуска
    (устаревшие "startup" и "shutdown" события).
"""

# ---------------------------------- Импорт стандартных библиотек
# ---------------------------------- Импорт сторонних библиотек
from contextlib import asynccontextmanager
from fastapi import FastAPI

# -------------------------------- Локальные модули
from core.models.db_helper import set_db_helper


# ----------------------------------------------------------------------------------------------------------------------
@asynccontextmanager
async def lifespan_db_dispose(app: FastAPI):
    """
        lifespan-менеджер закрытия соединения после выполнения запросов.
    """

    # "startup"
    yield

    # "shutdown"
    print('Закрытие подключения к базе данных')
    await set_db_helper.dispose()
