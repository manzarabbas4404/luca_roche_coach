from ast import mod
from pyexpat import model
from django.db import models

#  Create your models here.

class Register(models.Model):
     name = models.EmailField(max_length=50)
     password = models.CharField(max_length=50)
     Food_Plan_Summary_week_one = models.CharField(max_length=500)
     Food_Plan_Summary_week_one_chart = models.ImageField(upload_to=None, max_length=100)
     Food_Plan_Summary_week_two  = models.CharField(max_length=500)
     Food_Plan_Summary_week_two_chart  = models.ImageField(upload_to=None, max_length=100)
     Food_Plan_Summary_week_three  = models.CharField(max_length=500)
     Food_Plan_Summary_week_three_chart  = models.ImageField(upload_to=None, max_length=100)
     Food_Plan_Summary_week_four  = models.CharField(max_length=500)
     Food_Plan_Summary_week_four_chart  = models.ImageField(upload_to=None, max_length=100)

     Training_Plan_Summary_week_one  = models.CharField(max_length=500)
     Training_Plan_Summary_week_one_chart  = models.ImageField(upload_to=None, max_length=100)
     Training_Plan_Summary_week_two  = models.CharField(max_length=500)
     Training_Plan_Summary_week_two_chart  = models.ImageField(upload_to=None, max_length=100)
     Training_Plan_Summary_week_three  = models.CharField(max_length=500)
     Training_Plan_Summary_week_three_chart  = models.ImageField(upload_to=None, max_length=100)
     Training_Plan_Summary_week_four  = models.CharField(max_length=500)
     Training_Plan_Summary_week_four_chart  = models.ImageField(upload_to=None, max_length=100)

     Buy_week_one  = models.CharField(max_length=500)
     Buy_week_one_chart  = models.ImageField(upload_to=None, max_length=100)
     Buy_week_two  = models.CharField(max_length=500)
     Buy_week_two_chart  = models.ImageField(upload_to=None, max_length=100)
     Buy_week_three  = models.CharField(max_length=500)
     Buy_week_three_chart  = models.ImageField(upload_to=None, max_length=100)
     Buy_week_four  = models.CharField(max_length=500)
     Buy_week_four_chart  = models.ImageField(upload_to=None, max_length=100)

     Progress_week_one  = models.CharField(max_length=500)
     Progress_week_one_chart  = models.ImageField(upload_to=None, max_length=100)
     Progress_week_two  = models.CharField(max_length=500)
     Progress_week_two_chart  = models.ImageField(upload_to=None, max_length=100)
     Progress_week_three  = models.CharField(max_length=500)
     Progress_week_three_chart  = models.ImageField(upload_to=None, max_length=100)
     Progress_week_four  = models.CharField(max_length=500)
     Progress_week_four_chart  = models.ImageField(upload_to=None, max_length=100)

     My_measurements_and_progress  = models.CharField(max_length=500)
     The_summary_of_the_progression_curve  = models.CharField(max_length=500)
     Meal_close_to_the_training_summary  = models.CharField(max_length=500)
     Pre_post_recipe_data  = models.CharField(max_length=500)
     In_Case_recipe_data  = models.CharField(max_length=500)
     Meal_away_training_recipe_data  = models.CharField(max_length=500)
     Dessert_recipe_data  = models.CharField(max_length=500)