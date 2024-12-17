"""
    Модуль конфигураций, относящихся к API.
"""

# ---------------------------------- Импорт стандартных библиотек
# ---------------------------------- Импорт сторонних библиотек
from pydantic_settings import BaseSettings
from pydantic import BaseModel, PostgresDsn


# -------------------------------- Локальные модули


# ----------------------------------------------------------------------------------------------------------------------
class DatabaseConfig(BaseModel):
    url_db: PostgresDsn
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

    """

    run: RunConfig = RunConfig()
    api: PrefixAPI = PrefixAPI()
    db: DatabaseConfig # = DatabaseConfig()



# ======================================================================================================================
settings = Settings()
