from django.urls import path
from .views import ItemMenuList, PesananList, PesananDetail

urlpatterns = [
    path('menu/', ItemMenuList.as_view(), name='menu-list'),
    path('pesanan/', PesananList.as_view(), name='pesanan-list'),
    path('pesanan/<int:pk>/', PesananDetail.as_view(), name='pesanan-detail'),
]