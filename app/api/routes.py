from flask import Blueprint

from app.api.views import index_api, time_api

api = Blueprint('api', __name__)

api.add_url_rule('/',view_func=index_api)
api.add_url_rule('/time',view_func=time_api)
