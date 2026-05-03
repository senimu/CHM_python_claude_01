# routers/users.py
from fastapi import APIRouter

router = APIRouter(prefix="/users")

@router.get("")
def find_all():
    return ["Taro", "Hanako"]

@router.post("")
def create():
    return {"message": "Create a user"}

