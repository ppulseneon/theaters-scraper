from flask import jsonify, Blueprint

performances_controller = Blueprint('theaters_controller', __name__)

@performances_controller.route('/theaters/', methods=['GET'])
def get_performances():
    return jsonify()