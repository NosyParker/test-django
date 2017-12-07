import time
from django.shortcuts import render

from easycart import BaseCart
from core_app.models import ComplexDinner

class Cart(BaseCart):

    def add(self, pk, quantity=1):
        super(Cart, self).add(pk, quantity, timestamp=time.time())

    def get_queryset(self, pks):
        return ComplexDinner.objects.filter(pk__in=pks)
