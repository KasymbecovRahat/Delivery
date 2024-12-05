from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'users', UserProfileViewSet, basename='user_list')
router.register(r'categories', CategoryViewSet, basename='category_list')
router.register(r'contacts', ContactInfoViewSet, basename='contact')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'product-combos', ProductComboViewSet, basename='product_combo_list')
router.register(r'carts', CartViewSet, basename='cart')
router.register(r'cart-items', CartItemViewSet, basename='cart_items_list')
router.register(r'orders', OrdersViewSet, basename='order')
router.register(r'couriers', CourierViewSet, basename='courier')
router.register(r'store-reviews', StoreReviewViewSet, basename='store_review_list')
router.register(r'courier-reviews', CourierReviewViewSet, basename='courier_review_list')

urlpatterns = [
    path('', include(router.urls)),
    path('store/', StoreListAPIView.as_view(), name='store_list'),
    path('store/<int:pk>', StoreDetailAPIView.as_view(), name='store_detail'),
    path('create/', StoreCreateAPIView.as_view(), name='create_list'),
    path('create/<int:pk>/', StoreDetailUpdateDeleteAPIView.as_view(), name='store_edit'),
    path('add_product/', ProductCreateAPIView.as_view(), name='product_list'),
    path('add_product/<int:pk>', ProductDetailUpdateDeleteAPIView.as_view(), name='product_edit'),
    path('add_product_combo', ProductComboCreateAPIView.as_view(), name='product_combo_create'),
    path('add_product_combo/<int:pk>', ProductComboDetailUpdateDeleteAPIView.as_view(), name='product_combo_edit')

]