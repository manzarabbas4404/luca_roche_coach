from django.db import models

#  Create your models here.

class user_table(models.Model):
     name = models.EmailField(max_length=50)
     password = models.CharField(max_length=50)
     Food_Plan_Summary_week_one = models.CharField(max_length=500, null=True)
     Food_Plan_Summary_week_one_chart = models.ImageField(upload_to=None, max_length=100, null=True)
     Food_Plan_Summary_week_two  = models.CharField(max_length=500, null=True)
     Food_Plan_Summary_week_two_chart  = models.ImageField(upload_to=None, max_length=100, null=True)
     Food_Plan_Summary_week_three  = models.CharField(max_length=500, null=True)
     Food_Plan_Summary_week_three_chart  = models.ImageField(upload_to=None, max_length=100, null=True)
     Food_Plan_Summary_week_four  = models.CharField(max_length=500, null=True)
     Food_Plan_Summary_week_four_chart  = models.ImageField(upload_to=None, max_length=100, null=True)

     Training_Plan_Summary_week_one  = models.CharField(max_length=500, null=True)
     Training_Plan_Summary_week_one_chart  = models.ImageField(upload_to=None, max_length=100, null=True)
     Training_Plan_Summary_week_two  = models.CharField(max_length=500, null=True)
     Training_Plan_Summary_week_two_chart  = models.ImageField(upload_to=None, max_length=100, null=True)
     Training_Plan_Summary_week_three  = models.CharField(max_length=500, null=True)
     Training_Plan_Summary_week_three_chart  = models.ImageField(upload_to=None, max_length=100, null=True)
     Training_Plan_Summary_week_four  = models.CharField(max_length=500, null=True)
     Training_Plan_Summary_week_four_chart  = models.ImageField(upload_to=None, max_length=100, null=True)

     Buy_week_one  = models.CharField(max_length=500, null=True)
     Buy_week_one_chart  = models.ImageField(upload_to=None, max_length=100, null=True)
     Buy_week_two  = models.CharField(max_length=500, null=True)
     Buy_week_two_chart  = models.ImageField(upload_to=None, max_length=100, null=True)
     Buy_week_three  = models.CharField(max_length=500, null=True)
     Buy_week_three_chart  = models.ImageField(upload_to=None, max_length=100, null=True)
     Buy_week_four  = models.CharField(max_length=500, null=True)
     Buy_week_four_chart  = models.ImageField(upload_to=None, max_length=100, null=True)

     Progress_week_one  = models.CharField(max_length=500, null=True)
     Progress_week_one_chart  = models.ImageField(upload_to=None, max_length=100, null=True)
     Progress_week_two  = models.CharField(max_length=500, null=True)
     Progress_week_two_chart  = models.ImageField(upload_to=None, max_length=100, null=True)
     Progress_week_three  = models.CharField(max_length=500, null=True)
     Progress_week_three_chart  = models.ImageField(upload_to=None, max_length=100, null=True)
     Progress_week_four  = models.CharField(max_length=500, null=True)
     Progress_week_four_chart  = models.ImageField(upload_to=None, max_length=100, null=True)

     My_measurements_and_progress  = models.CharField(max_length=500, null=True)
     The_summary_of_the_progression_curve  = models.CharField(max_length=500, null=True)
     Meal_close_to_the_training_summary  = models.CharField(max_length=500, null=True)
     Pre_post_recipe_data  = models.CharField(max_length=500, null=True)
     In_Case_recipe_data  = models.CharField(max_length=500, null=True)
     Meal_away_training_recipe_data  = models.CharField(max_length=500, null=True)
     Dessert_recipe_data  = models.CharField(max_length=500, null=True)
     def __str__(self):
          return  self.name