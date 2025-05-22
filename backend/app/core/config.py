import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Garante que o .env seja carregado — ajuste o caminho conforme necessário
env_path = os.path.join(os.path.dirname(__file__), "..", "backend", ".env")
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = env_path  # redundância segura para fallback
        env_file_encoding = "utf-8"

settings = Settings()
