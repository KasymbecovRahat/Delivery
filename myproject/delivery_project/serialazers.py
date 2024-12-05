from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSimpleProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class ContactInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactInfo
        fields = ['contact_info', 'store']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'price', 'store', 'product_photo', ]


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'price', 'store', 'product_photo', ]


class ProductComboSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCombo
        fields = ['combo_name', 'combo_description',
                  'combo_price', 'combo_photo']


class ProductCreateComboSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCombo
        fields = ['combo_name', 'combo_description',
                  'combo_price', 'combo_photo']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CarItem
        fields = ['id', 'cart', 'product', 'quantity', 'get_total_price']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'create_date', 'items', 'get_total_price']


class OrdersSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    client_orders = UserProfileSerializer(read_only=True)
    courier_orders = UserProfileSerializer(read_only=True)

    class Meta:
        model = Orders
        fields = [
            'id', 'cart', 'product', 'client_orders', 'courier_orders',
            'orders_status', 'orders_created', 'delivery_address'
        ]


class CourierSerializer(serializers.ModelSerializer):
    users = UserProfileSerializer(read_only=True)
    current_orders = OrdersSerializer(read_only=True)

    class Meta:
        model = Courier
        fields = ['id', 'users', 'status_courier', 'current_orders']


class StoreReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d-%m-%Y  %H:%M'))

    class Meta:
        model = StoreReview
        fields = ['client',  'comment', 'rating', 'created_date']


class CourierReviewSerializer(serializers.ModelSerializer):
    client_review = UserProfileSerializer(read_only=True)
    courier = UserProfileSerializer(read_only=True)

    class Meta:
        model = CourierReview
        fields = ['id', 'client_review', 'courier', 'comment', 'rating']


class StoreDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    owner = UserSimpleProfileSerializer()
    contacts = ContactInfoSerializer(many=True, read_only=True)
    product = ProductSerializer(many=True, read_only=True)
    product_combo = ProductComboSerializer(read_only=True, many=True)
    review_store = StoreReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Store
        fields = ['id', 'store_name', 'store_description',
                  'owner', 'store_image', 'category', 'address',
                  'contacts', 'product', 'product_combo', 'review_store']


class StorelistSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()
    check_good = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = ['id', 'store_name',   'store_image', 'category',
                  'avg_rating', 'count_people', 'check_good']


    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()

    def get_check_good(self, obj):
        return obj.get_check_good()


class StoreSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_name', 'store_description', 'store_image',
                  'category', 'address', 'owner']

