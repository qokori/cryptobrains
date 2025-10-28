from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Currency
from .serializer import CurrencySerializer

class CurrencySetter(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer