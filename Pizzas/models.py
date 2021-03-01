from django.db import models
from django.db.models import Model

class Pizza(models.Model):
    Pizza_Type=models.CharField(max_length=20)
    Pizza_Size=models.CharField(max_length=20)
    Pizza_Toppings=models.CharField(max_length=20)

    def __str__(self):
        return  self.Pizza_Type




