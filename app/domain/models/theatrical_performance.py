import datetime

from peewee import AutoField, BooleanField, DateTimeField, CharField, IntegerField
from peewee import ForeignKeyField
from peewee_enum_field import EnumField

from app.domain.models.base import BaseModel
from app.domain.models.theater import Theater
from app.services.theater_service import TheaterService
from enum import Enum

from dataclasses import dataclass


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


@dataclass
class TheatricalPerformanceData:
    id: AutoField(primary_key=True)
    title: CharField()
    theater: ForeignKeyField(Theater.to_response(TheaterService.get_by_id(Theater)))
    type: CharField()
    description: CharField(null=True)
    age_restrictions: IntegerField(null=True)
    release_at: DateTimeField()
    day_of_week: EnumField(Weekday)
    preview_url: CharField(null=True)


class TheatricalPerformance(BaseModel):
    def __init__(self):
        """
                Модель объекта базы данных представления

                Attributes
                ----------
                self.id : AutoField
                    Id представления
                self.theater : ForeignKeyField
                    Театр, в котором будет представление
                self.title : CharField
                    Название представления
                self.type : CharField
                    Тип представления
                self.description : CharField
                    Описание представления (nullable)
                self.age_restrictions : IntegerField
                    Возрастные ограничения (nullable)
                self.release_at : DateTimeField
                    Время начала представления
                self.preview_url : CharField
                    Ссылка на превью (nullable)
                self.created_at : DateTimeField
                    Время создание записи в базу данных
                self.is_expired : BooleanField
                    Не прошло ли еще представление
                self.is_deleted : BooleanField
                    Не удалена ли запись из базы данных
            """
        super().__init__()
        # todo: учитывать сессии представлений (нужно ли?)

        self.id = AutoField(primary_key=True)
        self.theater = ForeignKeyField(Theater)
        self.title = CharField()
        self.type = CharField()
        self.description = CharField(null=True)
        self.age_restrictions = IntegerField(null=True)
        self.release_at = DateTimeField()
        self.day_of_week = EnumField(Weekday)
        self.preview_url = CharField(null=True)
        self.created_at = DateTimeField(default=datetime.datetime.now)
        self.is_expired = BooleanField(default=False)
        self.is_deleted = BooleanField(default=False)

    def to_response(self, t_performance) -> dict:
        theater = TheaterService.get_by_id(self.theater)

        return {
            'id': t_performance.id,
            'title': t_performance.title,
            'theater': Theater.to_response(theater),
            'type': t_performance.type,
            'description': t_performance.description,
            'age_restrictions': t_performance.age_restrictions,
            'release_at': t_performance.release_at,
            'day_of_week': t_performance.day_of_week,
            'preview_url': t_performance.preview_url
        }
