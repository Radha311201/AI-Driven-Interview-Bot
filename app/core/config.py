import os


class Settings:
    PROJECT_NAME: str = "AI-Driven-Interview-Bot"
    DEBUG: bool = os.getenv("DEBUG", "0") == "1"


settings = Settings()
