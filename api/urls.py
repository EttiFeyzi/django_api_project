from django.urls import path

from api.views import ProductCreate, ProductDetail, ProductList

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('new/', ProductCreate.as_view(), name='create'),

]
