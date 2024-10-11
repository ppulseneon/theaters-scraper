from app.api import app
from app.domain.models.base import database
from app.domain.models.performance import Performance
from app.domain.models.theater import Theater

tables = [Theater, Performance]

"""
    Инициализация базы данных, если она не создана
"""
def init():
    with database:
        database.create_tables(tables)
    create_default_values()

"""
    Инициализируем в базе данных значения по умолчанию
"""
def create_default_values():
    theaters = Theater.select()

    if len(theaters) > 0:
        return

    # todo: добавить логгирование

    opera_and_ballet_theatre = Theater.create(title='Донецкий театр оперы и балета',
        scrap_url='https://quicktickets.ru/doneck-teatr-opery-i-baleta')

    opera_and_ballet_theatre.save()