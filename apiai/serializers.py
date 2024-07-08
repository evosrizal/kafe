from rest_framework import serializers
from .models import Pesanan, ItemPesanan, ItemMenu

class ItemMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMenu
        fields = ['id', 'nama', 'deskripsi', 'harga', 'kategori']

class ItemPesananSerializer(serializers.ModelSerializer):
    item = ItemMenuSerializer()
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = ItemPesanan
        fields = ['item', 'jumlah', 'subtotal']

    def get_subtotal(self, obj):
        return obj.subtotal()

class PesananSerializer(serializers.ModelSerializer):
    item_pesanan = ItemPesananSerializer(source='itempesanan_set', many=True, read_only=True)
    total_harga = serializers.SerializerMethodField()

    class Meta:
        model = Pesanan
        fields = ['id', 'nomor_meja', 'item_pesanan', 'status', 'total_harga']

    def get_total_harga(self, obj):
        return obj.total_harga()
