from functools import lru_cache
from typing import Any, Dict, Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    """"""
    api_version: Optional[str] = "v1"
    api_url: Optional[str] = "http://127.0.0.1:8003"
    logger_config: Dict[str, Any] = {
        "version": 1,
            "disable_existing_loggers": False,
            "formatters": { 
                "standard": {
                    "format": "%(asctime)s [%(levelname)s] %(name)s %(lineno)s %(message)s"
                },
            },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "standard",
                "stream": "ext://sys.stdout"
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "WARNING",
                "filename": "logs/logs.log",
                "maxBytes": 10485760, # 10MB
                "formatter": "standard",
                "backupCount": 10,
                "encoding": "utf-8",
            }
        },
        "loggers": {
            "": {  # root logger
                "handlers": ["console", "file"],
                "level": "INFO",
                "propagate": False
            },
        }
    }

    class Config:
        env_file = ".env.dev"
        env_file_encoding = "utf-8"


@lru_cache(maxsize=128)
def get_settings():
    """"""
    return Settings()


settings = get_settings()
