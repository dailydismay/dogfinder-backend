import logging
import sys
from typing import List
from databases import DatabaseURL
from starlette.config import Config
from loguru import logger
from starlette.datastructures import CommaSeparatedStrings

config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

JWT_SECRET = config("JWT_SECRET")

CORS_ENDPOINTS: List[str] = config(
  "CORS_ENDPOINTS",
  cast=CommaSeparatedStrings,
  default="",
)

DB_URL = config("DB_URL", cast=DatabaseURL)
DB_MAX_POOL = config("DB_MAX_POOL", cast=int)
DB_MIN_POOL = config("DB_MIN_POOL", cast=int)

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
