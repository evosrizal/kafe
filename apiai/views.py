from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ItemMenu, Pesanan, ItemPesanan
from .serializers import ItemMenuSerializer, PesananSerializer

class ItemMenuList(APIView):
    def get(self, request):
        items = ItemMenu.objects.all()
        serializer = ItemMenuSerializer(items, many=True)
        return Response(serializer.data)

class PesananList(APIView):
    def get(self, request):
        pesanan = Pesanan.objects.all()
        serializer = PesananSerializer(pesanan, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PesananSerializer(data=request.data)
        if serializer.is_valid():
            pesanan = serializer.save()
            items_data = request.data.get('item_pesanan', [])
            for item_data in items_data:
                item = ItemMenu.objects.get(id=item_data['item']['id'])
                ItemPesanan.objects.create(pesanan=pesanan, item=item, jumlah=item_data['jumlah'])
            return Response(PesananSerializer(pesanan).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PesananDetail(APIView):
    def get_object(self, pk):
        try:
            return Pesanan.objects.get(pk=pk)
        except Pesanan.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pesanan = self.get_object(pk)
        serializer = PesananSerializer(pesanan)
        return Response(serializer.data)

    def put(self, request, pk):
        pesanan = self.get_object(pk)
        serializer = PesananSerializer(pesanan, data=request.data)
        if serializer.is_valid():
            pesanan = serializer.save()
            ItemPesanan.objects.filter(pesanan=pesanan).delete()
            items_data = request.data.get('item_pesanan', [])
            for item_data in items_data:
                item = ItemMenu.objects.get(id=item_data['item']['id'])
                ItemPesanan.objects.create(pesanan=pesanan, item=item, jumlah=item_data['jumlah'])
            return Response(PesananSerializer(pesanan).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pesanan = self.get_object(pk)
        pesanan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
