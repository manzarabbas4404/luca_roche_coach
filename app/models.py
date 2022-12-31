from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

#  Create your models here.

class user_table(models.Model):
     name = models.EmailField(max_length=50)
     password = models.CharField(max_length=50)
     Food_Plan_Week_Summary = models.CharField(max_length=500, null=True, blank=True)
     Food_Plan_Summary_week_one_chart = RichTextUploadingField(null=True, blank=True)
     Food_Plan_Summary_week_two_chart  = RichTextUploadingField(null=True, blank=True)
     Food_Plan_Summary_week_three_chart  = RichTextUploadingField(null=True, blank=True)
     Food_Plan_Summary_week_four_chart  = RichTextUploadingField(null=True, blank=True)

     Training_Plan_Week_Summary  = models.CharField(max_length=500, null=True, blank=True)
     Training_Plan_Summary_week_one_chart  = RichTextUploadingField(null=True, blank=True)
     Training_Plan_Summary_week_two_chart  = RichTextUploadingField(null=True, blank=True)
     Training_Plan_Summary_week_three_chart  = RichTextUploadingField(null=True, blank=True)
     Training_Plan_Summary_week_four_chart  = RichTextUploadingField(null=True, blank=True)

     Buy_week_summary  = models.CharField(max_length=500, null=True, blank=True)
     Buy_week_one_chart  = RichTextUploadingField(null=True, blank=True)
     Buy_week_two_chart  = RichTextUploadingField(null=True, blank=True)
     Buy_week_three_chart  = RichTextUploadingField(null=True, blank=True)
     Buy_week_four_chart  = RichTextUploadingField(null=True, blank=True)

     Progress_Week_summary  = models.CharField(max_length=500, null=True, blank=True)
     Progress_week_one_chart  = RichTextUploadingField(null=True, blank=True)
     Progress_week_two_chart  = RichTextUploadingField(null=True, blank=True)
     Progress_week_three_chart  = RichTextUploadingField(null=True, blank=True)
     Progress_week_four_chart  = RichTextUploadingField(null=True, blank=True)

     My_measurements_and_progress  = models.CharField(max_length=500, null=True, blank=True)
     The_summary_of_the_progression_curve  = models.CharField(max_length=500, null=True, blank=True)
     Meal_close_to_the_training_summary  = models.CharField(max_length=500, null=True, blank=True)
     Pre_post_recipe_data  = models.CharField(max_length=500, null=True, blank=True)
     In_Case_recipe_data  = models.CharField(max_length=500, null=True, blank=True)
     Meal_away_training_recipe_data  = models.CharField(max_length=500, null=True, blank=True)
     Dessert_recipe_data  = models.CharField(max_length=500, null=True, blank=True)
     def __str__(self):
          return  self.name