from peewee import Model, SqliteDatabase

database = SqliteDatabase('app/domain/storage/theaters.db')

class BaseModel(Model):
    """
        Базовая модель базы данных
    """
    class Meta:
        database = database