from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import authentication, products, categories, cart, checkout, orders, seller, admin

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authentication.router)
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(cart.router)
app.include_router(checkout.router)
app.include_router(orders.router)
app.include_router(seller.router)
app.include_router(admin.router)
