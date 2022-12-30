from django.db import models
from catalog.models import Catalog


class Category(models.Model):
    name = models.CharField(max_length=120)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


