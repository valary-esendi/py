from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_name = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=100)  # e.g., 'Protein', 'Fat'
    times_consumed = models.IntegerField(default=0)
    food_expiration = models.DateField()

    def __str__(self):
        return self.meal_name
