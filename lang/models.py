from djmoney.models.fields import MoneyField
from django.db import models
from djmoney.contrib.exchange.models import convert_money
from django.utils.translation import gettext as _


class Item(models.Model):
    name = models.CharField(max_length=100, blank=True)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='GBP', help_text='Amount in GBP', null=True, blank=True)
    quantity = models.IntegerField(blank=True)

    @property
    def amount_translated(self):
        currency_code = _("Currency Code")
        return convert_money(self.amount, currency_code)

    def __str__(self):
        return self.name