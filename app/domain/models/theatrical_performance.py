import datetime
from dataclasses import dataclass

from peewee import AutoField, BooleanField, DateTimeField, CharField, IntegerField
from peewee import ForeignKeyField
from peewee_enum_field import EnumField

from app.domain.models.base import BaseModel
from app.domain.models.review import Review
from app.domain.models.theater import Theater
from app.enums.weekdays import Weekday
from app.services.performance_service import PerformanceService
from app.services.theater_service import TheaterService

@dataclass
class TheatricalPerformance(BaseModel):
    """
        Модель объекта базы данных представления

        Attributes
        ----------
        self.id : AutoField
            Id представления
        self.theater_id : ForeignKeyField
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

    id = AutoField(primary_key=True)
    theater_id = ForeignKeyField(Theater)
    title = CharField()
    type = CharField()
    description = CharField(null=True)
    age_restrictions = IntegerField(null=True)
    release_at = DateTimeField()
    day_of_week = EnumField(Weekday)
    preview_url = CharField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    is_expired = BooleanField(default=False)
    is_deleted = BooleanField(default=False)

    @staticmethod
    def to_response_list(data: list['TheatricalPerformance']) -> list[dict]:
        return [TheatricalPerformance.to_response(performance) for performance in data]

    @staticmethod
    def to_response(data: 'TheatricalPerformance') -> dict:
        theater = TheaterService.get_by_id(data.theater_id)
        reviews = PerformanceService.get_reviews(data.id)

        return {
            'id': data.id,
            'title': data.title,
            'theater_id': Theater.to_response(theater),
            'type': data.type,
            'description': data.description,
            'age_restrictions': data.age_restrictions,
            'release_at': data.release_at,
            'day_of_week': data.day_of_week,
            'preview_url': data.preview_url,
            'reviews': Review.to_response_list(reviews)
        }
