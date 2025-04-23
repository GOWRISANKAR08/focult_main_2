
from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date = models.DateField(auto_now_add=True)
    