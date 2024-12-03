from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "E-commerce API"
    database_url: str = "mongodb://localhost:27017"

    class Config:
        env_file = ".env"

settings = Settings()
