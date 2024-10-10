from peewee import *

from app.domain.models.performance import Performance
from app.domain.models.theater import Theater

database = SqliteDatabase('theaters.db')
tables = [Theater, Performance]

def create_tables():
    # todo: если database.tables is not created, то вызвать add_default_data()

    with database:
        database.create_tables(tables)

def add_default_data():
    # todo: заполнить театрами по умолчанию
    pass