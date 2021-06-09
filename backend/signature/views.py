from django.shortcuts import render
from braces.views import CsrfExemptMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateSignatureSerializer
# Create your views here.


class AddSignatureView(CsrfExemptMixin, APIView):
    """Добавление подписи"""

    def post(self, request):
        authentication_classes = []
        serializer = CreateSignatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Подпись успешно добавлена"}, status=201)
        else:
            return Response(serializer.errors, status=400)

    def get_permissions(self):
        if self.request.method == 'POST':
            return []
        return super().get_permissions()
