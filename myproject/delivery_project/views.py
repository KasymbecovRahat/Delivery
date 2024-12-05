from rest_framework import viewsets, permissions, generics
from .models import *
from .serialazers import *
from .permissions import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StorelistSerializer


class StoreDetailAPIView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer
    permission_classes = [CheckStatus, CheckStoreOrders]


class StoreCreateAPIView(generics.CreateAPIView):
    serializer_class = StoreSerialazer
    permission_classes = [CheckStatus]


class StoreDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerialazer
    permission_classes = [CheckStatus, CheckStoreOwner, CheckStoreOrders]


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
    permission_classes = [CheckStatus]


class ProductDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [CheckStatus, CheckStoreOwner, CheckStoreOrders]


class ProductComboViewSet(viewsets.ModelViewSet):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboSerializer


class ProductComboCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductCreateComboSerializer
    permission_classes = [CheckStatus]


class ProductComboDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = ProductCreateComboSerializer
    permission_classes = [CheckStatus, CheckStoreOwner, CheckStoreOrders]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CarItem.objects.all()
    serializer_class = CartItemSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [CheckStoreOrders]


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class StoreReviewViewSet(viewsets.ModelViewSet):
    queryset = StoreReview.objects.all()
    serializer_class = StoreReviewSerializer


class CourierReviewViewSet(viewsets.ModelViewSet):
    queryset = CourierReview.objects.all()
    serializer_class = CourierReviewSerializer

