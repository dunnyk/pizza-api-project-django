from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status


# Create your views here.


class HelloOrderView(generics.GenericAPIView):

    def get(self, request):
        name = {'greeting': 'Good morning From Order'}
        return Response(name, status=status.HTTP_200_OK)
