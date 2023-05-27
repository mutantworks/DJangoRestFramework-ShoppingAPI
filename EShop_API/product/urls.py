from django.urls import path

from .views import ProductCreate, ProductsList, ProductDetail, CategoryList, CategoryDetail, CategoryUpdate

urlpatterns = [
    path('products_list/', ProductsList.as_view()),
    path('categories_list/', CategoryList.as_view()),
    path('product_create/', ProductCreate.as_view()),
    path('product_detail/<str:name>/', ProductDetail.as_view()),
    path('category_detail/<str:name>/', CategoryDetail.as_view()),
    path('category_update/<str:name>/', CategoryUpdate.as_view()),
]