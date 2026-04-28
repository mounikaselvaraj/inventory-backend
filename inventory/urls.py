from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.items_list_create),
    path('items/<int:pk>/', views.item_detail),
]

