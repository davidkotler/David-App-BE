from fastapi import APIRouter
from fastapi.params import Header
from db.dependency import get_db
from fastapi import Depends
from dnotes.db.Crud.NoteCrud import NoteCrud, create_note_crud
from dnotes.schemas.notes import NoteCreate, NoteUpdate
from dnotes.auth.token import get_current_user



router = APIRouter()







# @router.get("/", status_code=200)
# def get_all_notes(start_date: int = 0, end_date: int = 0):
#     crud = create_note_crud()
#     if start_date and end_date:
#         notes = crud.get_all()
#     else:
#         notes = crud.get_all()
#     return notes


# @router.get("/", status_code=200)
# def get_all_notes(start_date: int = 0, end_date: int = 0, current_user: str = Depends(get_current_user)):
#     """
#     get all notes of specific user
#     :param start_date:
#     :param end_date:
#     :param current_user:
#     :return:
#     """
#     crud = create_note_crud()
#     return crud.get_all(current_user)

@router.get("/", status_code=200)
def get_all_notes(current_user: str = Depends(get_current_user)):
    """
    get all notes of specific user

    """
    print("enter get funcion")
    crud = create_note_crud()
    #add comments
    notes = crud.get_all(current_user)
    return notes


@router.get("/{note_id}", status_code=200)
def get_note(note_id):
    crud = create_note_crud()
    notes = crud.get_all(note_id)
    return notes


@router.post("/", status_code=200)
def create_note(note: NoteCreate):
    crud = create_note_crud()
    new_note = crud.create(note)
    return new_note


@router.put("/{note_id}")
def update_note(note_id, note: NoteUpdate):
    crud = create_note_crud()
    new_note = crud.update(note_id, note)
    return new_note


@router.delete("/{note_id}")
def delete_note(note_id):
    crud = create_note_crud()
    crud.delete(note_id)
    return True