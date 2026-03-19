from fastapi import APIRouter, Depends
outer = APIRouter()

@router.post("/cart")
def add_to_cart():
    # add to cart logic
    pass
