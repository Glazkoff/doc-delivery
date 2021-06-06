from rest_framework import serializers
from .models import Order, Courier

# Сериализация заказов и курьеров


class CourierDetailSerializer(serializers.ModelSerializer):
    """Полное представление курьера"""

    class Meta:
        model = Courier
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    """Полное представление проекта"""
    courier = CourierDetailSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class OrdersListSerializer(serializers.ModelSerializer):
    """Полное представление списка проектов"""

    courier = CourierDetailSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
    """Добавление задачи"""
    class Meta:
        model = Order
        # fields = '__all__'
        fields = ("departure_date", "cost", "salary_part",
                  "address_from", "address_to", "sender", "recipient", "pointFromLat", "pointFromLng", "pointToLat", "pointToLng")

    # def create(self, validated_data):
    #     return Order.objects.update_or_create(courier=validated_data.get(
    #         "courier", None), defaults={"salary_part": validated_data.get("salary_part", None)})
