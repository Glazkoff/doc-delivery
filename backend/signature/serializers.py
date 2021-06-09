from .models import Signature
from rest_framework import serializers


class CreateSignatureSerializer(serializers.ModelSerializer):
    """Полное представление подписи"""

    class Meta:
        model = Signature
        fields = '__all__'
