from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderSerializerForCreate(serializers.ModelSerializer):
    order_id = serializers.CharField(max_length=256)
    product_name = serializers.CharField(max_length=256)
    user_id = serializers.IntegerField()
    user_name = serializers.CharField(max_length=256)
    restaurant_name = serializers.CharField(max_length=256)
    quantity = serializers.IntegerField(min_value=1)


    class Meta:
        model = Order
        fields = (
            'order_id',
            'product_name',
            'user_id',
            'user_name',
            'restaurant_name',
            'quantity'
        )

    def validate(self, data):
        if (
                'order_id' not in data or
                'product_name' not in data or
                'user_id' not in data or
                'user_name' not in data or
                'restaurant_name' not in data or
                'quantity' not in data
        ):
            raise ValidationError({
                'message': 'one or more required fields are missing'
            })

        return data

    def create(self, validated_data):
        order_id = validated_data['order_id']
        product_name = validated_data['product_name']
        user_id = validated_data['user_id']
        restaurant_name = validated_data['restaurant_name']
        user_name = validated_data['user_name']
        quantity = validated_data['quantity']

        order = Order.objects.create(
            order_id=order_id,
            product_name=product_name,
            user_id=user_id,
            user_name=user_name,
            restaurant_name=restaurant_name,
            quantity=quantity
        )

        return order