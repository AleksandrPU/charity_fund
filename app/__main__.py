import asyncio
import logging

import uvicorn

from app.init_db import create_first_superuser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создаём root-пользователя.
asyncio.run(create_first_superuser())

# Запускаем приложение.
logger.info("Запуск приложения...")
try:
    uvicorn.run(
        app="app.main:app",
        host="127.0.0.1",
        port=8000,
        workers=1,
    )
except KeyboardInterrupt:
    logger.info("Выход из приложения.")
