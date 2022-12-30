from django.db import models
from django.utils import timezone
from category.models import Category


class Product(models.Model):
    FINGERPRINT = (
        ('S', 'Back'),
        ('M', 'Front'),
        ('L', 'Side'),
        ('N', 'Null'),
    )
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(default='default_product.jpg')
    description = models.TextField()
    create_at = models.DateTimeField(default=timezone.now)
    memory = models.CharField(max_length=16, null=True, blank=True)
    ram = models.CharField(max_length=16, null=True, blank=True)
    camera1 = models.CharField(max_length=16, null=True, blank=True)
    camera2 = models.CharField(max_length=16, null=True, blank=True)
    battery = models.CharField(max_length=16, null=True, blank=True)
    fingerprint = models.CharField(max_length=1, choices=FINGERPRINT, null=True, blank=True)
    face_unlock = models.BooleanField(null=True, blank=True)
    processor = models.CharField(max_length=32, null=True, blank=True)
    country = models.CharField(max_length=32, null=True, blank=True)
    company = models.CharField(max_length=32, null=True, blank=True)
    size = models.CharField(max_length=16, null=True, blank=True)
    weight = models.CharField(max_length=16, null=True, blank=True)
    sim = models.CharField(max_length=1, choices=(('1', '1'), ('2', '2'),), null=True, blank=True)
    colors = models.CharField(max_length=16, null=True, blank=True)
    electr = models.CharField(max_length=16, null=True, blank=True)
    volume = models.CharField(max_length=16, null=True, blank=True)
    max_weight = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True)
    display = models.BooleanField(null=True, blank=True)
    wifi = models.BooleanField(null=True, blank=True)
    def __str__(self):
        return self.name


# class ProductTable(models.Model):
#     caregory = models.ForeignKey(Category, on_delete=models.CASCADE)
#     count = models.IntegerField()
#     def __str__(self):
#         return f'{self.count} {self.caregory.name}'
