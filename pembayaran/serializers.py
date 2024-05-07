from rest_framework import serializers
from .models import Pembayaran

class PembayaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembayaran
        fields = ['id', 'pesanan', 'total_bayar', 'metode_pembayaran', 'waktu_pembayaran']
