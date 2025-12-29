import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application settings"""
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    DATABASE_URL: str = "sqlite:///./content.db"
    DEBUG: bool = True
    
    
    DEFAULT_MODEL: str = "gpt-3.5-turbo"
    DEFAULT_IMAGE_SIZE: str = "1024x1024"
    DEFAULT_TEMPERATURE: float = 0.7
    DEFAULT_MAX_TOKENS: int = 500

settings = Settings()
