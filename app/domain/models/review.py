import datetime

from peewee import AutoField, ForeignKeyField, CharField, DateTimeField, BooleanField

from app.domain.models.base import BaseModel
from app.domain.models.theatrical_performance import TheatricalPerformance


class Review(BaseModel):
    def __init__(self):
        """
            Модель объекта базы данных отзывов

            Attributes
            ----------
            self.id : AutoField
                Id отзыва
            self.performance : ForeignKeyField
                Ключ представления, к которому оставлен отзыв
            self.author : CharField
                Имя автора
            self.text : CharField
                Содержимое отзыва
            self.added_at : DateTimeField
                Время добавления комментария на сайт для скрапа (изначальное)
            self.created_at : DateTimeField
                Время создания записи
            self.is_deleted : BooleanField
                Не удалена ли запись из базы
        """
        super().__init__()
        self.id = AutoField(primary_key=True)
        self.performance = ForeignKeyField(TheatricalPerformance)
        self.author = CharField()
        self.text = CharField()
        self.added_at = DateTimeField(null=True)
        self.created_at = DateTimeField(default=datetime.datetime.now)
        self.is_deleted = BooleanField(default=False)
