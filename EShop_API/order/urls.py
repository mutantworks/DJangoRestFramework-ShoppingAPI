from django.urls import path

from .views import OrderCreate, OrdersList, OrderDetails, OrderUpdate

urlpatterns = [
    path('order_create/', OrderCreate.as_view()),
    path('orders_list/', OrdersList.as_view()),
    path('order_delete/<int:pk>/', OrderDetails.as_view()),
    path('order_update/<int:pk>/', OrderUpdate.as_view())
]