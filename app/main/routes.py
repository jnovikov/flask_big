from flask import Blueprint, render_template
from app.main.views import index_page, redirect_page
from app import app

main = Blueprint('main', __name__, template_folder='templates')

main.add_url_rule("/", view_func=index_page)
main.add_url_rule("/redirect", view_func=redirect_page)
