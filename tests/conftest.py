import logging
import pytest
from pydantic_settings import BaseSettings, SettingsConfigDict

class AdminAuth(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    username: str
    password: str


@pytest.fixture
def admin_auth() -> AdminAuth:
    return AdminAuth()
