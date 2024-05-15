from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list


@dataclass
class Config:
    tg_bot: TgBot
    database_path: str


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    tg_bot = TgBot(token=env("TOKEN"), admin_ids=env.list("ADMINS"))
    return Config(
        tg_bot=tg_bot,
        database_path=env("DB_PATH"),
    )
