from flask import jsonify

from app.domain.models.theatrical_performance import TheatricalPerformance


def get_performances_response(performances: list[TheatricalPerformance]) -> jsonify:
    """
        Метод формирует ответ для запроса на получение представлений
    """

    result = [TheatricalPerformance().to_response(performance) for performance in performances]
    return jsonify({'performances': result})