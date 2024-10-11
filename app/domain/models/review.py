import datetime

from peewee import AutoField, ForeignKeyField, CharField, DateTimeField, BooleanField

from app.domain.models.base import BaseModel
from app.domain.models.performance import Performance


class Review(BaseModel):
    """
        Модель объекта базы данных отзывов

        Attributes
        ----------
        id : AutoField
            Id отзыва
        performance : ForeignKeyField
            Ключ представления, к которому оставлен отзыв
        author : CharField
            Имя автора
        text : CharField
            Содержимое отзыва
        added_at : DateTimeField
            Время добавления комментария на сайт для скрапа (изначальное)
        created_at : DateTimeField
            Время создания записи
        is_deleted : BooleanField
            Не удалена ли запись из базы
    """

    id = AutoField(primary_key=True)
    performance = ForeignKeyField(Performance)
    author = CharField()
    text = CharField()
    added_at = DateTimeField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    is_deleted = BooleanField(default=False)
