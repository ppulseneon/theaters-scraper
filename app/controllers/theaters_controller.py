from flask import jsonify, Blueprint

from app.domain.models.theater import Theater
from app.services.theater_service import TheaterService

theaters_controller = Blueprint('theaters_controller', __name__)

@theaters_controller.route('/theaters/', methods=['GET'])
def get_theaters():
    theaters = TheaterService.get_all()
    result = [Theater.to_response(theater) for theater in theaters]

    return jsonify({'theaters': result})