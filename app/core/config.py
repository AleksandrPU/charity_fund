# import os
from typing import Optional

# import structlog
from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'QRKot'
    app_description: str = 'Фонд собирает пожертвования на различные проекты.'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    postgres_user: str = 'fastapi'
    postgres_password: str = 'mysecretpassword'
    postgres_db: str = 'fastapi'
    secret: str = 'secret'
    # token_lifetime: int = 3600
    token_lifetime: int = 360000
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()

# Set up the logger
# log_level = os.getenv("LOG_LEVEL", "DEBUG")
# log_format = os.getenv("LOG_FORMAT", "JSON")
# log_service = os.getenv("LOG_SERVICE_NAME", "unknown")


# def add_service(_, __, event_dict: dict) -> dict:
#     event_dict["service"] = log_service
#     return event_dict


# log_processors = [
#     structlog.stdlib,
#     structlog.stdlib.add_logger_name,
#     structlog.processors.TimeStamper(fmt="iso"),
#     structlog.processors.CallsiteParameterAdder(
#         [
#             structlog.processors.CallsiteParameter.FILENAME,
#             structlog.processors.CallsiteParameter.FUNC_NAME,
#             structlog.processors.CallsiteParameter.LINENO,
#         ],
#     ),
#     structlog.stdlib.add_log_level,
#     structlog.processors.StackInfoRenderer(),
#     structlog.processors.format_exc_info,
#     structlog.processors.ExceptionPrettyPrinter(),
#     add_service,
# ]


# Make sure that the renderers are last in processors
# if log_format.lower() == "json":
#     log_processors.append(structlog.processors.JSONRenderer())
# else:
#     # Console renderer
#     log_processors.append(structlog.dev.ConsoleRenderer())


# python3.11 has this mapping built into the logging module.
# https://docs.python.org/3/library/logging.html#logging-levels
# LOG_LEVEL_MAPPER = {
#     "CRITICAL": 50,
#     "ERROR": 40,
#     "WARNING": 30,
#     "INFO": 20,
#     "DEBUG": 10,
#     "NOTSET": 0,
# }
# log_level_int = LOG_LEVEL_MAPPER[log_level]
# wrapper = structlog.make_filtering_bound_logger(log_level_int)
# structlog.configure(
#     processors=log_processors,
#     wrapper_class=wrapper
# )


# logger = structlog.get_logger()
