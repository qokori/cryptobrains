from rest_framework import serializers
from .models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    to_usd = serializers.FloatField()

    class Meta:
        model = Currency
        fields = '__all__'