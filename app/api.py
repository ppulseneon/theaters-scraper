from flask import app, Flask

from app.controllers.performances_controller import performances_controller

app = Flask(__name__)
app.register_blueprint(performances_controller)

def run():
    app.run(host='0.0.0.0', port=8080)