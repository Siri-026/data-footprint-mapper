from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str
    
    # Redis
    REDIS_URL: str
    
    # APIs
    HIBP_API_KEY: str = ""  # Optional, has free tier
    
    # Security
    RATE_LIMIT_PER_HOUR: int = 10
    
    class Config:
        env_file = ".env"

settings = Settings()
