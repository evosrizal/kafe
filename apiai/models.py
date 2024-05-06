from django.db import models

class ItemMenu(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

class Pesanan(models.Model):
    nomor_meja = models.IntegerField()
    item = models.ManyToManyField(ItemMenu, through='ItemPesanan')
    status = models.CharField(max_length=20, default='pending')

    def total_harga(self):
        return sum(item.harga for item in self.item.all())

    def __str__(self):
        return f"Pesanan {self.id} - Meja {self.nomor_meja}"

class ItemPesanan(models.Model):
    pesanan = models.ForeignKey(Pesanan, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemMenu, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.item.harga * self.jumlah
