from flask import Blueprint, render_template
from app.main.views import index_page, redirect_page
from app.main.controllers import IndexPageController, ListNotesController
from app import app

main = Blueprint('main', __name__, template_folder='templates')

main.add_url_rule("/", view_func=IndexPageController.as_view("index"))
main.add_url_rule('/list_notes',view_func=ListNotesController.as_view("list_notes"))
main.add_url_rule("/redirect", view_func=redirect_page)
