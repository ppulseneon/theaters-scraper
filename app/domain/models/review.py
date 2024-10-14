import datetime
from dataclasses import dataclass

from peewee import AutoField, ForeignKeyField, CharField, DateTimeField, BooleanField

from app.domain.models.base import BaseModel
from app.domain.models.theatrical_performance import TheatricalPerformance


@dataclass
class Review(BaseModel):
    """
        Модель объекта базы данных отзывов

        Attributes
        ----------
        id : AutoField
            Id отзыва
        performance_id : ForeignKeyField
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
    performance_id = ForeignKeyField(TheatricalPerformance)
    author = CharField()
    text = CharField()
    added_at = DateTimeField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    is_deleted = BooleanField(default=False)

    @staticmethod
    def to_response_list(reviews: list['Review']) -> list[dict]:
        return [Review.to_response(review) for review in reviews]

    @staticmethod
    def to_response(data: 'Review') -> dict:
        return {
            'id': data.id,
            'author': data.author,
            'performance_id': data.performance_id,
            'text': data.text
        }