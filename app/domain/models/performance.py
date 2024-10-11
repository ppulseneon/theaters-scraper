import datetime

from peewee import AutoField, BooleanField, DateTimeField, CharField, IntegerField
from peewee import ForeignKeyField

from app.domain.models.base import BaseModel
from app.domain.models.theater import Theater


class Performance(BaseModel):
    """
        Модель объекта базы данных представления
    """

    # todo: представить day_of_week как одно из значений списка ['Понедельник', 'Вторник', 'Среда']

    # todo: реализовать таблицу комментариев и хранить здесь комментарии (отзывы)

    # todo:

    id = AutoField(primary_key=True)
    theater = ForeignKeyField(Theater)
    title = CharField()
    type = CharField()
    description = CharField(null=True)
    age_restrictions = IntegerField(null=True)
    release_at = DateTimeField()
    day_of_week = CharField()
    preview_url = CharField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    is_expire = BooleanField(default=False)
    is_deleted = BooleanField(default=False)