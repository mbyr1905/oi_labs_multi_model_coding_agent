from fastapi import APIRouter
from routes.auth import auth_router
from routes.products import products_router
from routes.orders import orders_router
from routes.admin import admin_router
from routes.seller import seller_router

router = APIRouter()

router.include_router(auth_router, prefix='/auth')
router.include_router(products_router, prefix='/products')
router.include_router(orders_router, prefix='/orders')
router.include_router(admin_router, prefix='/admin')
router.include_router(seller_router, prefix='/seller')