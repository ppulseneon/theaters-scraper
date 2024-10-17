import datetime
from dataclasses import dataclass

from peewee import AutoField, BooleanField, DateTimeField, CharField, IntegerField, ForeignKeyField
from peewee import ForeignKeyField

from app.domain.models.base import BaseModel
from app.domain.models.review import Review
from app.domain.models.session import TheatricalSession
from app.domain.models.theater import Theater
from app.services.performance_service import PerformanceService
from app.services.session_service import SessionService
from app.services.theater_service import TheaterService

@dataclass
class TheatricalPerformance(BaseModel):
    """
        Модель объекта базы данных представления

        Attributes
        ----------
        id : AutoField
            Id представления
        theater_id : ForeignKeyField
            Театр, в котором будет представление
        title : CharField
            Название представления
        type : CharField
            Тип представления
        description : CharField
            Описание представления (nullable)
        age_restrictions : IntegerField
            Возрастные ограничения (nullable)
        preview_url : CharField
            Ссылка на превью (nullable)
        self.created_at : DateTimeField
            Время создание записи в базу данных
        self.is_expired : BooleanField
            Не прошло ли еще представление
        self.is_deleted : BooleanField
            Не удалена ли запись из базы данных
            """

    id: AutoField = AutoField(primary_key=True)
    theater_id: ForeignKeyField = ForeignKeyField(Theater)
    title: CharField = CharField()
    type: CharField = CharField()
    description: CharField = CharField(null=True)
    age_restrictions: IntegerField = IntegerField(null=True)
    preview_url: CharField = CharField(null=True)
    created_at: DateTimeField = DateTimeField(default=datetime.datetime.now)
    is_deleted: BooleanField = BooleanField(default=False)

    @staticmethod
    def to_response_list(data: list['TheatricalPerformance']) -> list[dict]:
        return [TheatricalPerformance.to_response(performance) for performance in data]

    @staticmethod
    def to_response(data: 'TheatricalPerformance') -> dict:
        theater = TheaterService.get_by_id(data.theater_id)
        reviews = PerformanceService.get_reviews(data.id)
        sessions = SessionService.get_sessions(data.id)

        return {
            'id': data.id,
            'title': data.title,
            'theater_id': Theater.to_response(theater),
            'type': data.type,
            'description': data.description,
            'age_restrictions': data.age_restrictions,
            'preview_url': data.preview_url,
            'sessions': TheatricalSession.to_response_list(sessions),
            'reviews': Review.to_response_list(reviews)
        }
