from app.domain.models.review import Review
from app.domain.models.session import TheatricalSession
from app.domain.models.theatrical_performance import TheatricalPerformance
from app.services.session_service import SessionService


class PerformanceService:
    """
        Сервис для работы с представлениями театров
    """

    @staticmethod
    def get_all() -> list[TheatricalPerformance]:
        """
            Метод для получения всех представлений
        """
        performances = TheatricalPerformance.get(TheatricalPerformance.is_deleted is not True)
        return performances

    @staticmethod
    def get_active():
        """
            Метод для получения активных представлений
        """

        result = []

        performances = TheatricalPerformance.get(TheatricalPerformance.is_deleted is not True)

        for performance in performances:
            sessions = SessionService.get_sessions(performance.id)

            if len(sessions) > 0:
                result.append(performance)

        return result

    @staticmethod
    def get_reviews(performance_id: int):
        """
            Метод для получения отзывов на представления
        """
        reviews = Review.get(Review.performance_id is performance_id)
        return reviews