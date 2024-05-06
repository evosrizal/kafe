from django.contrib import admin
from .models import ItemMenu, Pesanan, ItemPesanan
from pembayaran.models import Pembayaran

class PembayaranInline(admin.StackedInline):
    model = Pembayaran

@admin.register(Pesanan)
class PesananAdmin(admin.ModelAdmin):
    inlines = [PembayaranInline]

@admin.register(ItemMenu)
class ItemMenuAdmin(admin.ModelAdmin):
    pass

@admin.register(ItemPesanan)
class ItemPesananAdmin(admin.ModelAdmin):
    pass

@admin.register(Pembayaran)
class PembayaranAdmin(admin.ModelAdmin):
    list_display = ('pesanan', 'total_bayar', 'metode_pembayaran', 'waktu_pembayaran')
    list_filter = ('metode_pembayaran', 'waktu_pembayaran')
    search_fields = ('pesanan__nomor_meja',)

    def nomor_meja(self, obj):
        return obj.pesanan.nomor_meja
    nomor_meja.short_description = 'Nomor Meja'