from django.urls import path
from .views import CurrencySetter

urlpatterns = [
    path('currencies/set', CurrencySetter.as_view()),
]
    