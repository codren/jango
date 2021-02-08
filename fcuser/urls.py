from django.urls import path
from . import views     # view와 연결하기 위함

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
]
