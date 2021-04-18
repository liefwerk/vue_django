from django.contrib.auth.models import User
from django.db import models

from product.models import Product

class Order(models.Model):
  user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=100)
  place = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  stripe_token = models.CharField(max_length=100)

  class Meta:
    # this orders the orders with the date, so it's easier to see it in the backend
    ordering = ['-created_at',]
    
  def __str__(self):
    # this return the first name of the user who created the order when we call the Order
    return self.first_name

# getting each item as a separate entity as well
class OrderItem(models.Model):
  # referencing to the order
  order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
  # referencing to the product to know which product it is on the item
  product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
  # to easily get the price without going through the product
  price = models.DecimalField(max_digits=8, decimal_places=2)
  # quantity defaults to 1
  quantity = models.IntegerField(default=1)

  def __str__(self):
    return '%s' % self.id