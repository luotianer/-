# form_1/serializers.py
from rest_framework import serializers
from .models import Category, Dish

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'description', 'price', 'image', 'is_available']

class CategorySerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'dishes']

class CreateOrderSerializer(serializers.Serializer):
    customer_name = serializers.CharField(max_length=50)
    items = serializers.ListField(
        child=serializers.DictField(
            child=serializers.IntegerField()
        )
    )

    def validate_customer_name(self, value):
        base = value
        counter = 1
        while Customer.objects.filter(name=value).exists():
            value = f"{base}{counter}"
            counter += 1
        return value