from pydantic import BaseModel, BaseSettings


class Settings(BaseSettings):
    env: str = "dev"
    db_str = "sqlite:////C:/projects/david_app/pythonProject2/dnotes/db.sqlite"

settings = Settings()
