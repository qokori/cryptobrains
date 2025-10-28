from django.db import models
import requests

class Currency(models.Model):
    code = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100, unique=True)
    is_favorite = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True)
    to_usd_cached = models.FloatField(null=True, blank=True, editable=False)

    @property
    def to_usd(self):
        try:
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={self.code}&vs_currencies=usd"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            price = data[self.code]['usd']
            self.to_usd_cached = price
            self.save(update_fields=['to_usd_cached', 'updated_at'])
            return price
        except Exception as e:
            print(f'Ошибка получения курса для {self.name}: {e}')
            if self.to_usd_cached is not None:
                return self.to_usd_cached
            return None