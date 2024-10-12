from app.domain.models.theater import Theater

class TheaterService:

    """
        Сервис работы с театрами
    """

    @staticmethod
    def get_all() -> list[Theater]:
        theaters = Theater.select().where(Theater.is_deleted == False)
        return theaters