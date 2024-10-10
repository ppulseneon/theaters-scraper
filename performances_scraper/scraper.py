import requests
from bs4 import BeautifulSoup

from performances_scraper.constants import quicktickets_url


class PerformancesScraper:
    def __init__(self, theaters):
        self.theaters = theaters

    def scrap(self):
        # todo: реализовать подбор типа скрапа из объекта театра по типу полю типа подбора
        pass

    def _scrap_by_quicktickets(self, theater):
        response = requests.get(theater.site_url)

        # todo: формировать результат в модель представления

        if response.status_code != 200:
            return False

        soup = BeautifulSoup(response.text, 'html.parser')
        result = []

        list_elements = soup.find(id='elems-list')
        div_elements = list_elements.find_all('div')
        for div in div_elements:
            performance = {}

            c_elem = div.find(class_='c')
            if c_elem is None:
                continue

            name = c_elem.find(class_='underline').text
            age = c_elem.find(class_='ageRestriction').text
            description = c_elem.find(class_='d').text
            more = quicktickets_url + c_elem.find(class_='more')['href']
            buy = quicktickets_url + c_elem.find(class_='b').find(class_='notUnderline')['href']

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

            result.append(performance)

        return result
