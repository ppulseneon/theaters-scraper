from flask import Blueprint, jsonify

from app.models.responses.performances_response import get_performances_response
from app.services.performance_service import PerformanceService

performances_controller = Blueprint('performances_controller', __name__)

@performances_controller.route('/performances/', methods=['GET'])
def get_performances():
    performances = PerformanceService.get_active()
    return get_performances_response(performances)

@performances_controller.route('/performances/history', methods=['GET'])
def get_performances_history():
    # todo: реализовать получение выступлений за участок времени
    return jsonify()
