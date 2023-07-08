from django.db import models
from user.models import User

drinkChoices = [
    ('0', 'lạnh'),
    ('1', 'nóng'),
]

sizeChoices = [
    ('0', 'M'),
    ('1', 'L'),
]

sugarChoices = [
    ('0', '70%'),
    ('1', '30%'),
    ('2', '100%'),
    ('3', '50%'),
    ('4', 'Không đường'),
]

toppingChoices = [
    ('0', 'Trân trâu sương mai'),
    ('1', 'Trân châu hoàng kim'),
    ('2', 'Thạch Konjac'),
    ('3', 'Thạch cafe'),
    ('4', 'Thạch Machiato'),
]

# Create your models here.
class Product(models.Model):
    image = models.ImageField(null = True, blank = True, upload_to="product")
    name = models.CharField(max_length = 116)
    price = models.IntegerField(default = 0)

    def __str__(self):
        return self.name
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    drinkType = models.CharField(default = 0, choices = drinkChoices)
    sizeType = models.CharField(default = 0, choices = sizeChoices)
    sugarType = models.CharField(default = 0, choices = sugarChoices)
    toppingType = models.CharField(default = 0, choices = toppingChoices)
    price = models.IntegerField(default = 0)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    cartItem = models.ManyToManyField(CartItem)

    def __str__(self):
        return self.user.username