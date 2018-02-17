from flask import Flask

app = Flask(__name__)

from app.main.routes import main as main_blueprint
from app.api.routes import api as api_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint, url_prefix='/api')