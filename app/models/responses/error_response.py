from flask import jsonify


def get_error_response(status_code: int, error_type: str, message: str) -> jsonify():
    """
        Метод формирует ошибочный ответ
    """
    return jsonify({'error_type': error_type, 'error_message': message}), status_code