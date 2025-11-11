from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    HUGGINGFACE_API_KEY: str
    LITELLM_MASTER_KEY: str
    LITELLM_SALT_KEY: str
    DATABASE_URL: str
    UI_USERNAME: str
    UI_PASSWORD: str
    SAMPLE_API_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()