from app.domain.models.theater import Theater

class TheaterService:
    """
        Сервис работы с театрами
    """

    @staticmethod
    def get_all() -> list[Theater]:
        theaters = Theater.get(Theater.is_deleted is not True)
        return theaters

    @staticmethod
    def get_by_id(id) -> Theater:
        theater = Theater.get(Theater.id == id and Theater.is_deleted is not True)
        return theater