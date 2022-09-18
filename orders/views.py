from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from . import serializers
from . models import Order
User = get_user_model()


# Create your views here.


class HelloOrderView(generics.GenericAPIView):

    def get(self, request):
        name = {'greeting': 'Good morning From Order'}
        return Response(name, status=status.HTTP_200_OK)


class OrderCreateListAPIView(generics.GenericAPIView):

    serializer_class = serializers.OrderCreationSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, )
    orders = Order.objects.all()

    def get(self, request):
        serializer = self.serializer_class(instance=self.orders, many=True)
        return_messagge = {
            "message": "all orders displayed",
            "data": serializer.data,
        }
        return Response(return_messagge, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        user = request.user
        if serializer.is_valid(raise_exception=True):
            serializer.save(customer=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    permission_classes = (IsAdminUser, )

    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id):
        data = request.data
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(
            data=data, instance=order, many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        if order:
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateOrderStatusView(generics.GenericAPIView):
    serializer_class = serializers.OrderStatusUpdateSerializer
    permission_classes = (IsAdminUser, )

    def put(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        data = request.data
        serializer = self.serializer_class(data=data, instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserOrdersView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer

    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        orders = Order.objects.filter(customer=user)
        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserOrderDetailView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer

    def get(self, request, user_id, order_id):
        user = User.objects.get(pk=user_id)
        order = Order.objects.filter(customer=user).get(pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(serializer.data, status=status.HTTP_200_OK)
