from flask import jsonify

from app.domain.models.theater import Theater

def get_theaters_response(theaters: list[Theater]) -> jsonify:
    """
        Метод формирует ответ для запроса на получение театров
    """

    result = Theater.to_response_list(theaters)
    return jsonify({'theaters': result})