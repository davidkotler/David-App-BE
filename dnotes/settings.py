from pydantic import BaseModel, BaseSettings


class Settings(BaseSettings):
    env: str = "dev"
    # db_str = "sqlite:////C:/projects/david_app/pythonProject2/dnotes/db.sqlite"
    db_str = "sqlite:///./sql_app.db"
    db_port = "5432"

settings = Settings()
