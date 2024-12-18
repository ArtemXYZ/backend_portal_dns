"""
    Модуль конфигураций, относящихся к API.
"""

# ---------------------------------- Импорт стандартных библиотек
# ---------------------------------- Импорт сторонних библиотек
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn


# -------------------------------- Локальные модули


# ----------------------------------------------------------------------------------------------------------------------
class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False,
    echo_pool: bool = False,
    pool_size: int = 50,
    max_overflow: int = 10,


class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8080

class PrefixAPI(BaseModel):
    prefix: str = '/dns_api'


class Settings(BaseSettings):
    """
        Класс управления настройками api. Все зависимости вынесены и собраны в одном месте для удобства.

        Можно в текущем классе просто указать, например:
            host: str
            port: int
            db_url: str
            api_prefix: str
        однако, по мере роста класс будет расти и лучше сразу разделить сущности.
        В связи с этим структура класса будет иметь настоящий вид.

        model_config: APP_CONFIG__DB__URL="postgresql+asyncpg://user:pasword@localhost:5432/mydatabase"
    """

    run: RunConfig = RunConfig()
    api: PrefixAPI = PrefixAPI()
    db: DatabaseConfig  # = DatabaseConfig()
    # Конфигурация подключения к базе данных:
    model_config = SettingsConfigDict(
        case_sensitive=False,  # Игнорировать регистр.
        env_nested_delimiter='__',  # Указываем разделитель для вложенных объектов. APP_CONFIG__DB__URL
        env_prefix='APP_CONFIG__',
        env_file='.env',  # Где будет считывать.
    )



# ======================================================================================================================
settings = Settings()
