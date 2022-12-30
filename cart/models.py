from django.db import models
from product.models import Product
from users.models import CustomUser


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
