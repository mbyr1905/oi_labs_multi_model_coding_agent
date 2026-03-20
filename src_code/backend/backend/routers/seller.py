from fastapi import APIRouter, Depends
from backend.services import UserService

router = APIRouter()

@router.get("/seller")
def get_seller():
    user_service = UserService()
    seller = user_service.get_seller()
    return seller
