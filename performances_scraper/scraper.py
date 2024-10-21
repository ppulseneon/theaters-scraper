import bs4
import requests
from bs4 import BeautifulSoup

from app.domain.models.theater import Theater
from app.enums.scrap_type import ScrapTypes
from performances_scraper.constants import QUICK_TICKETS_URL


class PerformancesScraper:

    def __init__(self, theaters: list | Theater):
        """
        :param theaters: Театры которые нужно обработать
        """
        self.theaters = [theaters] if isinstance(theaters, Theater) else theaters

    def scrap_multiple_theaters(self) -> list[dict[str, str | list]]:
        """

        :return: данные о времени и стоимости билетов на выступления с нескольких театров
        """
        results = []
        for theater in self.theaters:
            result = None
            if theater.scrap_type == ScrapTypes.quick_tickets:
                result = self.scrap_by_quick_tickets(theater)
            if result:
                results.extend(result)

        return results

    def scrap_by_quick_tickets(self, theater: Theater) -> list[dict[str, str | list]] | None:
        """
        :param theater: Информация о конкретном театре. Подойдёт только quick tickets.
        :return: Данные об активных представлениях.
        """
        theater_url = str(theater.site_url)
        response = requests.get(theater_url, timeout=20)

        # todo: формировать результат в модель представления
        # todo: скрапить информацию непосредственно из more_ref для полноты картины

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        result = []

        list_elements = soup.find(id='elems-list')
        div_elements = list_elements.find_all('div')
        for div in div_elements:
            subres = self.__parse_quick_tickets_div(div)
            if subres is not None:
                result.append(subres)
        return result

    @staticmethod
    def __parse_quick_tickets_div(div: bs4.element) -> dict[str, str | list] | None:
        """
        Обработка каждого собранного div из elems-list
        :param div: не нуждается в представлении
        :return: В теории должен возвращать TheatricalPerformance класс
        """
        performance = {}

        c_elem = div.find(class_='c')
        if c_elem is None:
            return None

        name = c_elem.find(class_='underline').text
        age = c_elem.find(class_='ageRestriction').text
        description = c_elem.find(class_='d').text
        more = QUICK_TICKETS_URL + c_elem.find(class_='more')['href']
        buy = QUICK_TICKETS_URL + c_elem.find(class_='b').find(class_='notUnderline')['href']

        sessions = []
        sessions_elems = c_elem.find_all('div', attrs={'class': 'session-column'})
        for session_elem in sessions_elems:
            if session_elem is not None:
                time_elem = session_elem.find(class_='underline')

                if time_elem is not None:
                    sessions.append(time_elem.text)

        # todo: реализовать получение фото представления
        # todo: реализовать получение ссылок на бронь сессий

        performance['name'] = name
        performance['age'] = age
        performance['description'] = description
        performance['more'] = more
        performance['buy'] = buy
        performance['sessions'] = sessions

        return performance
