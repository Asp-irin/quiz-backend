from pydantic import BaseSettings


class Settings(BaseSettings):
    random_string_length: int = 20
