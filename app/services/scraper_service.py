from time import sleep

from app.domain.models.performance import Performance
from app.services.performance_service import PerformanceService
from app.services.theater_service import TheaterService
from performances_scraper.scraper import PerformancesScraper


class ScraperService:
    """
        Сервис работы со скрапером представлений театров
    """

    @staticmethod
    def update_performances():
        """
            Метод для постоянного скрапинга и обновлений представлений из театров
        """

        while True:
            scraped_performances = ScraperService.scrap_performances()
            db_performances = PerformanceService.get_all()

            # todo: реализовать поиск представления в системе,
            #       добавление новых и привязку к театру,
            #       помечение флагом is_expired и

            sleep(100)


    @staticmethod
    def scrap_performances() -> list[Performance]:
        """
            Метод для получения актуальных представлений из театров
        """
        theaters = TheaterService.get_all()

        scraper = PerformancesScraper(theaters)
        result = scraper.scrap()

        return result