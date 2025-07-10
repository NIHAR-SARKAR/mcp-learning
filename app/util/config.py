from dotenv import load_dotenv
import os

class Settings:
    load_dotenv()

    MODEL_URL: str = os.getenv("MODEL_URL", "MODEL_URL")
    MODEL_API_KEY: str = os.getenv("MODEL_API_KEY", "MODEL_API_KEY")
    DATABASE_URL: float = os.getenv("DATABASE_URL", "DATABASE_URL")
    MODEL_API_VERSION: float = os.getenv("MODEL_API_VERSION", "MODEL_API_VERSION")
    MODEL_NAME: float = os.getenv("MODEL_NAME", "MODEL_NAME")
    MODEL_DEPLOYMENT: float = os.getenv("MODEL_DEPLOYMENT", "MODEL_DEPLOYMENT")
    DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "db-test",
    "user": "user_x",
    "password": "pass2025"
    }

    class Config:
        env_file = ".env"

settings = Settings()