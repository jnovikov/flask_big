from collections import OrderedDict


class Note(object):
    def __init__(self, id, text):
        self.id = id
        self.text = text

    def __repr__(self):
        return "<Note Id -- {}, Text -- {}>".format(self.id, self.text)
    def __str__(self):
        return "<Note Id -- {}, Text -- {}>".format(self.id,self.text)



class NoteModel(object):
    notes = [Note(0,"KEK")]

    @staticmethod
    def list_notes():
        return NoteModel.notes

    @staticmethod
    def add_note(text):
        if (len(NoteModel.notes)) > 0:
            last = NoteModel.notes[-1]
            new_id = last.id + 1
        else:
            new_id = 0
        note = Note(new_id, text)
        NoteModel.notes.append(note)

    @staticmethod
    def get_by_id(id):
        try:
            note = NoteModel.notes[id]
        except IndexError:
            return None
        else:
            return note