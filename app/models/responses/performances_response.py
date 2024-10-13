from flask import jsonify

from app.domain.models.performance import Performance


def get_performances_response(performances: list[Performance]) -> jsonify:
    """
        Метод формирует ответ для запроса на получение представлений
    """

    result = [Performance.to_response(performance) for performance in performances]
    return jsonify({'performances': result})