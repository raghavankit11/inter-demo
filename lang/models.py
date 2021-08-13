from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100, blank=True)
    # amount = models.MoneyField(blank=True, help_text="Amount in GBP")
    quantity = models.IntegerField(blank=True)


    def __str__(self):
        return self.name