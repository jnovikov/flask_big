from flask.views import View
from flask import request, render_template, jsonify

from app.main.service import get_notes

class PolymorphicController(View):
    def get_objects(self):
        raise NotImplementedError("ALLO REALISUY METOD")

    def get_template(self):
        raise NotImplementedError("ALLO REALISUY METOD")

    def get_view_type(self):
        return "html"

    def dispatch_request(self):
        objects = self.get_objects()
        view_type = self.get_view_type()
        if view_type == "html":
            return render_template(self.get_template(), objects=objects)
        return jsonify(objects)


class IndexPageController(PolymorphicController):

    def get_objects(self):
        return []

    def get_template(self):
        return "index.html"


class ListNotesController(PolymorphicController):

    def get_objects(self):
        return get_notes()

    def get_view_type(self):
        return "html"

    def get_template(self):
        return "list.html"
