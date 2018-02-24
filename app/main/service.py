from app.main.models import NoteModel


def get_notes():
    return [x.__dict__ for x in NoteModel.list_notes()]
