from flask import Blueprint, jsonify

performances_controller = Blueprint('performances_controller', __name__)

@performances_controller.route('/performances/', methods=['GET'])
def get_performances():
    # todo: реализовать получение текущих выступлений
    return jsonify()

@performances_controller.route('/performances/history', methods=['GET'])
def get_performances_history():
    # todo: реализовать получение выступлений за участок времени
    return jsonify()
