from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(null = True, blank = True, upload_to="product")
    name = models.CharField(max_length = 116)
    description = models.TextField()
    price = models.IntegerField(default = 0)

    def __str__(self):
        return self.name