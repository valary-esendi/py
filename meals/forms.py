from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['meal_name', 'meal_type', 'times_consumed', 'food_expiration']