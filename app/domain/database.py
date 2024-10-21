from app.domain.models.base import database
from app.domain.models.theatrical_performance import TheatricalPerformance
from app.domain.models.theater import Theater
from app.enums.scrap_type import ScrapTypes

tables = [Theater, TheatricalPerformance]

"""
    Инициализация базы данных, если она не создана
"""
def init():
    with database:
        database.create_tables(tables)
    create_default_values()

"""
    Инициализируем в базе данных значения по умолчанию
"""
def create_default_values():
    theaters = Theater.select()

    if len(theaters) > 0:
        return

    # todo: добавить логгирование



    opera_and_ballet_theatre = Theater.create(
        title='Донецкий театр оперы и балета',
        description='Донецкий государственный академический театр оперы и балета является неотъемлемой частью культуры Донбасса. '
                    'За 90 лет своего существования он вписал яркую страницу в летопись театрального искусства.'
                    'Коллективом театра осуществлено более 300 постановок опер, балетов, оперетт, музыкальных комедий,'
                    'детских музыкальных сказок по произведениям отечественных и зарубежных композиторов, а также современных авторов.'
                    'Нет ни одного признанного классического произведения, с которым театр не'
                    'познакомил бы донецкого зрителя за период своей творческой деятельности.',
        site_url='https://donbassopera.ru',
        scrap_url='https://quicktickets.ru/doneck-teatr-opery-i-baleta',
        scrap_type=ScrapTypes.quick_tickets,
        image_url='https://upload.wikimedia.org/wikipedia/commons/f/f0/Donezk_Zentrum_Oper.JPG',
        address='Донецкая народная республика, Донецк, ул. Артёма, д. 82',
        contact_phone='+7(856) 304-60-19')

    opera_and_ballet_theatre.save()