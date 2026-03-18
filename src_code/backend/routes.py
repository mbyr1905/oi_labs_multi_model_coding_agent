from fastapi import APIRouter
from authentication.routes import authentication_router
from product.routes import product_router
from cart.routes import cart_router
from order.routes import order_router
from seller.routes import seller_router
from admin.routes import admin_router

router = APIRouter()

router.include_router(authentication_router, prefix='/auth')
router.include_router(product_router, prefix='/products')
router.include_router(cart_router, prefix='/cart')
router.include_router(order_router, prefix='/orders')
router.include_router(seller_router, prefix='/sellers')
router.include_router(admin_router, prefix='/admins')