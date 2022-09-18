from rest_framework import serializers
from .models import Order


class OrderCreationSerializers(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.HiddenField(default='PENDING')#use hiddenfield because superuser only see this while updating
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ['size', 'order_status', 'quantity', 'id']


class OrderDetailSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.CharField(default='PENDING')
    quantity = serializers.IntegerField()
    create_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model=Order
        fields = ['id', 'size', 'order_status', 'quantity', 'create_at', 'updated_at']


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(default='PENDING')

    class Meta:
        model=Order
        fields=['order_status']