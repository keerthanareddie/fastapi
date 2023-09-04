from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    #model_config = SettingsConfigDict(case_sensitive=True)
    database_hostname :str = 'localhost'
    database_port: str ='5432'
    database_password: str = 'keerthana24'
    database_name: str ='fastapi'
    database_username: str ='postgres'
    secret_key: str = 'keeerthana'
    algorithm: str = 'HS256'
    access_token_expire_minutes: int = '60'

settings = Settings()

class Config:
    env_file = ".env"