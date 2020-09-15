from django.db import models

class PizzaModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)