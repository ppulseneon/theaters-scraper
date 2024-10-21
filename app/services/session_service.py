from app.domain.models.session import TheatricalSession
from peewee import AutoField

class SessionService:
    """
        Сервис работы с сессиями представлений
    """

    @staticmethod
    def get_sessions(performance_id: AutoField):
        """
            Метод для получения отзывов на представления
        """
        sessions = TheatricalSession.get(TheatricalSession.performance_id is performance_id
                                         and TheatricalSession.is_expired is False
                                         and TheatricalSession.is_deleted is False)
        return sessions