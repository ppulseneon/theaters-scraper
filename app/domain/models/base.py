from peewee import Model

from app.domain.database import database


class BaseModel(Model):
    """
        Базовая модель базы данных
    """
    class Meta:
        database = database