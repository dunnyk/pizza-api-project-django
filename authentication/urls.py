from django.urls import path
from . import views


urlpatterns = [
    path('auth/', views.HelloAuthView.as_view(), name='main'),
    path('signup/', views.UserCreateView.as_view(), name='sign_up'),
]
