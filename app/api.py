from flask import app, Flask

from app.controllers.performances_controller import performances_controller
from app.controllers.theaters_controller import theaters_controller
from app.domain import database

app = Flask(__name__)
app.register_blueprint(performances_controller)
app.register_blueprint(theaters_controller)

def run():
    database.init()
    app.run(host='0.0.0.0', port=8080)