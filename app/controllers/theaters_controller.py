from flask import Blueprint

from app.models.responses.theaters_responses import get_theaters_response
from app.services.theater_service import TheaterService

theaters_controller = Blueprint('theaters_controller', __name__)

@theaters_controller.route('/theaters/', methods=['GET'])
def get_theaters():
    """
        Роут для получения всех театров
    """

    theaters = TheaterService.get_all()
    return get_theaters_response(theaters)