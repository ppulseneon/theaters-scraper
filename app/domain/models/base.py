from peewee import Model, SqliteDatabase

theaters_database = SqliteDatabase('app/domain/storage/theaters.db')

class BaseModel(Model):
    """
        Базовая модель базы данных

        Attributes
        ----------
        database : SqliteDatabase
            Объект базы данных
    """
    class Meta:
        database = theaters_database