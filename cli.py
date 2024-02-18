from accounting_bot.config import DB_NAME, DB_PASSWORD, DB_USER, DB_HOST, DB_PORT

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError
from accounting_bot.entity import BaseEntity


def drop_database_with_sqlalchemy():
    try:
        # Создание подключения к базе данных PostgreSQL
        engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

        with engine.connect() as connection:
            BaseEntity.metadata.drop_all(bind=engine)

        print("База данных успешно удалена")

    except ProgrammingError as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    drop_database_with_sqlalchemy()
