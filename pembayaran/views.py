from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pembayaran
from .serializers import PembayaranSerializer

class PembayaranList(APIView):
    def get(self, request):
        pembayaran = Pembayaran.objects.all()
        serializer = PembayaranSerializer(pembayaran, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PembayaranSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PembayaranDetail(APIView):
    def get_object(self, pk):
        try:
            return Pembayaran.objects.get(pk=pk)
        except Pembayaran.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        pembayaran = self.get_object(pk)
        serializer = PembayaranSerializer(pembayaran)
        return Response(serializer.data)

    def put(self, request, pk):
        pembayaran = self.get_object(pk)
        serializer = PembayaranSerializer(pembayaran, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pembayaran = self.get_object(pk)
        pembayaran.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
