import datetime

from peewee import DateTimeField, AutoField, ForeignKeyField, CharField, BooleanField
from peewee_enum_field import EnumField

from app.domain.models.base import BaseModel
from app.domain.models.theatrical_performance import TheatricalPerformance
from app.enums.weekdays import Weekday

class TheatricalSession(BaseModel):
    """
        Модель объекта базы данных сессии представления

        Attributes
        ----------
        id : AutoField
            Id представления
        performance_id: ForeignKeyField
            Id представления
        release_at: DateTimeField
            Время начала сессии
        day_of_week: EnumField
            День недели начала сессии
        purchase_url: CharField
            Ссылка на страницу бронирования билетов
        is_expired: BooleanField
            Закончилась ли сессия
        created_at: DateTimeField
            Время создания сессии в бд
        is_deleted: BooleanField
            Удалена ли сессия из бд
    """

    id: AutoField = AutoField(primary_key=True)
    performance_id: ForeignKeyField = ForeignKeyField(TheatricalPerformance)
    release_at: DateTimeField = DateTimeField()
    day_of_week: EnumField = EnumField(Weekday)
    purchase_url: CharField = CharField(null=True)
    is_expired: BooleanField = BooleanField(default=False)
    created_at: DateTimeField = DateTimeField(default=datetime.datetime.now)
    is_deleted: BooleanField = BooleanField(default=False)

    @staticmethod
    def to_response_list(sessions: list['TheatricalSession']) -> list[dict]:
        return [TheatricalSession.to_response(session) for session in sessions]

    @staticmethod
    def to_response(session: 'TheatricalSession') -> dict:
        return {
            'id': session.id,
            'performance': session.performance_id,
            'release_at': session.release_at,
            'day_of_week': session.day_of_week,
            'purchase_url': session.purchase_url,
            'is_expired': session.is_expired,
        }