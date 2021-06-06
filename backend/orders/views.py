from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order, Courier
from .serializers import OrderDetailSerializer, OrdersListSerializer, CreateOrderSerializer
from braces.views import CsrfExemptMixin

# Create your views here.


class OrdersListView(CsrfExemptMixin, APIView):
    """Вывод списка заказов"""

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrdersListSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        authentication_classes = []
        serializer = CreateOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Заказ успешно добавлен"}, status=201)
        else:
            return Response(serializer.errors, status=400)

    def get_permissions(self):
        if self.request.method == 'POST':
            return []
        return super().get_permissions()


class OrderDetailView(APIView):
    """Вывод одного заказа"""

    def get(self, request, pk):
        try:
            order = Order.objects.get(id=pk)
            serializer = OrderDetailSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            # запросу не соответствует ни один элемент.
            return Response({})
        except Order.MultipleObjectsReturned:
            # запросу соответствует несколько элементов.
            return Response({})
