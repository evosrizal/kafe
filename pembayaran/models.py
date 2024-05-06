from django.db import models
from apiai.models import Pesanan

class Pembayaran(models.Model):
    pesanan = models.OneToOneField(Pesanan, on_delete=models.CASCADE)
    total_bayar = models.DecimalField(max_digits=10, decimal_places=2)
    metode_pembayaran = models.CharField(max_length=50)
    waktu_pembayaran = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pembayaran untuk Pesanan {self.pesanan.id}"