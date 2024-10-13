from app.domain.models.performance import Performance


class PerformanceService:
    """
        Сервис для работы с представлениями театров
    """

    @staticmethod
    def get_all() -> list[Performance]:
        performances = Performance.get(Performance.is_deleted is not True)
        return performances

    @staticmethod
    def get_active():
        performances = Performance.get(Performance.is_deleted is not True
                                       and Performance.is_expire is not True)
        return performances