from django.contrib.auth.models import User
from django.urls import reverse
from djmoney.models.fields import MoneyField
from django.db import models
from djmoney.contrib.exchange.models import convert_money
from django.utils.translation import gettext as _

from core import settings


class Item(models.Model):
    name = models.CharField(max_length=100, blank=True)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='GBP', null=True, blank=True)
    quantity = models.IntegerField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True, db_index=True, editable=False,
                                      help_text='Datetime on which this record was created.')
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False,
                                      help_text='Datetime on which this record was last modified.')

    @property
    def amount_translated(self):
        currency_code = _("Currency Code")
        return convert_money(self.amount, currency_code)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('lang:items', kwargs={'pk': self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    timezone = models.CharField(max_length=40, null=True, blank=True, choices=settings.TIME_ZONES)


class Post(models.Model):
    text_content = models.CharField(max_length=100, null=True, blank=True)

