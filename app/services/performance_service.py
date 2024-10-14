from app.domain.models.theatrical_performance import TheatricalPerformance


class PerformanceService:
    """
        Сервис для работы с представлениями театров
    """

    @staticmethod
    def get_all() -> list[TheatricalPerformance]:
        performances = TheatricalPerformance.get(TheatricalPerformance.is_deleted is not True)
        return performances

    @staticmethod
    def get_active():
        performances = TheatricalPerformance.get(TheatricalPerformance.is_deleted is not True
                                                 and TheatricalPerformance.is_expire is not True)
        return performances