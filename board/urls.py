from django.urls import path
from . import views     # view와 연결하기 위함

urlpatterns = [
    path('list/', views.board_list),
    path('write/', views.board_write),
    path('detail/<int:pk>/', views.board_detail),
]
