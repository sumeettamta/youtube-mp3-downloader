from django.db import models
from downloads.models import Songs
from User.models import User

class CartItem(models.Model):
    user = models.ForeignKey(User, default=1)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    song = models.ForeignKey(Songs, blank=False, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.cart_id)

    class Meta:
        db_table = 'cart_items'
        ordering = ['updated']

    def total(self):
        return self.quantity * self.song.price

    def price(self):
        return self.song.price
