from rest_framework import serializers
from .models import Pesanan, ItemPesanan, ItemMenu

class ItemMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMenu
        fields = ['id', 'nama', 'deskripsi', 'harga', 'kategori']

class ItemPesananSerializer(serializers.ModelSerializer):
    # Menggunakan tautan reverse untuk ItemMenuSerializer
    item = ItemMenuSerializer()

    class Meta:
        model = ItemPesanan
        fields = ['item', 'jumlah', 'subtotal']

class PesananSerializer(serializers.ModelSerializer):
    item_pesanan = ItemPesananSerializer(many=True, read_only=True)

    class Meta:
        model = Pesanan
        fields = ['id', 'nomor_meja', 'item_pesanan', 'status', 'total_harga']
