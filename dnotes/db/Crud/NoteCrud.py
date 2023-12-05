from db.dependency import get_db
from dnotes.db.Models import note_model as Note
from dnotes.db.example_db import notes,Notes,users
from fastapi.encoders import jsonable_encoder
from dnotes.schemas.notes import NoteCreate, NoteUpdate




class NoteCrud:
    def __init__(self, db):
        self.db = db

    def create(self, note: NoteCreate):  # add new note to the notes dictionary
        new_id = max(Notes.keys()) + 1
        Notes[new_id] = {
            "id":new_id,
            "title": note.title,
            "content": note.content
        }
        return 1

    def get_all(self, user):
        """
         get all notes of single user

        """
        return jsonable_encoder(notes[user])


    def get_by_id(self, note_id: int):
        print(note_id)
        return notes[int(note_id)]


    def update(self,note_id, note: NoteUpdate):

        Notes[int(note_id)]= {
            "id":int(note_id),
            "title": note.title,
            "content": note.content
        }

    def delete(self, note_id):
        Notes.pop(int(note_id))

def create_note_crud():
    db = get_db()
    crud = NoteCrud(db=db)
    return crud


