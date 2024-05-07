from django.urls import path
from .views import PembayaranList, PembayaranDetail

urlpatterns = [
    path('pembayaran/', PembayaranList.as_view(), name='pembayaran-list'),
    path('pembayaran/<int:pk>/', PembayaranDetail.as_view(), name='pembayaran-detail'),
]
