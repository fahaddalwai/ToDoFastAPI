import os

# Imports
from pydantic import BaseSettings, validator
from dotenv import load_dotenv

# Loading .env file
load_dotenv()


class AppSettings(BaseSettings):
    title: str = "FA-TODO API"
    description: str = "GDSC TODO API made using FastAPI"
    version: str = "0.0.1"


class Settings(BaseSettings):
    database_username: str
    database_server: str
    database_password: str
    database_hostname: str
    database_name: str
    cors_origin_whitelist: str

    @validator('cors_origin_whitelist')
    def split_cors_origin_string(cls, cors_origin_whitelist):

        return cors_origin_whitelist.split(',')

    class Config:
        env_file = r"C:\Users\dalwa\Desktop\app\.env.example"


app_settings = AppSettings()
settings = Settings()