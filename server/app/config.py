from typing import Literal

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST"]
    LOG_LEVEL: str

    SQLITE_PLUGINS: str
    SQLITE_DB_URL: str
    SQLITE_DB_URL_TEST: str

    POSTGRES_PLUGINS: str
    POSTGRES_DB_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    @property
    def DATABASE_URL(self):
        if self.MODE == 'DEV':
            return (f'{self.SQLITE_PLUGINS}:///{self.SQLITE_DB_URL}')
        elif self.MODE == 'TEST':
            return (f'{self.SQLITE_PLUGINS}:///{self.SQLITE_DB_URL_TEST}')
        
    # @property
    # def DATABASE_URL(self):
    #     if self.MODE == 'DEV':
    #         return (f'{self.POSTGRES_PLUGINS}://{self.POSTGRES_USER}:'
    #                 f'{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:'
    #                 f'{self.POSTGRES_PORT}/{self.POSTGRES_DB_NAME}')
        # elif self.MODE == 'TEST':
        #     return (f'postgresql+asyncpg://{self.TEST_PG_USER}:'
        #             f'{self.TEST_PG_PASSWORD}@{self.TEST_PG_HOST}:'
        #             f'{self.TEST_PG_PORT}/{self.TEST_PG_DB_NAME}')
        
    model_config = SettingsConfigDict(env_file='.env')

settings=Settings()




    # POSTGRES_TEST_DB_NAME: str
    # POSTGRES_TEST_USER: str
    # POSTGRES_TEST_PASSWORD: str
    # POSTGRES_TEST_HOST: str
    # POSTGRES_TEST_PORT: int

    # SECRET_KEY: str
    # ALGORITHM: str

    # SECRET: str
    # PASSWORD: str


    