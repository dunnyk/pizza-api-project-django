from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserCreationSerializer


# Create your views here.

class HelloAuthView(generics.GenericAPIView):

    @swagger_auto_schema(operation_summary="hello auth")
    def get(self, request):
        dan = {'name': 'kaimbigo'}
        return Response(data=dan, status=status.HTTP_200_OK)


class UserCreateView(generics.GenericAPIView):
    serializer_class = UserCreationSerializer

    @swagger_auto_schema(operation_summary="create an account....")
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
