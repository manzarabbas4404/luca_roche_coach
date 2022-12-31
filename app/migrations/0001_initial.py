# Generated by Django 3.2.16 on 2022-12-28 13:02

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('Food_Plan_Summary_week_one', models.CharField(blank=True, max_length=500, null=True)),
                ('Food_Plan_Summary_week_one_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Food_Plan_Summary_week_two', models.CharField(blank=True, max_length=500, null=True)),
                ('Food_Plan_Summary_week_two_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Food_Plan_Summary_week_three', models.CharField(blank=True, max_length=500, null=True)),
                ('Food_Plan_Summary_week_three_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Food_Plan_Summary_week_four', models.CharField(blank=True, max_length=500, null=True)),
                ('Food_Plan_Summary_week_four_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Training_Plan_Summary_week_one', models.CharField(blank=True, max_length=500, null=True)),
                ('Training_Plan_Summary_week_one_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Training_Plan_Summary_week_two', models.CharField(blank=True, max_length=500, null=True)),
                ('Training_Plan_Summary_week_two_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Training_Plan_Summary_week_three', models.CharField(blank=True, max_length=500, null=True)),
                ('Training_Plan_Summary_week_three_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Training_Plan_Summary_week_four', models.CharField(blank=True, max_length=500, null=True)),
                ('Training_Plan_Summary_week_four_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Buy_week_one', models.CharField(blank=True, max_length=500, null=True)),
                ('Buy_week_one_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Buy_week_two', models.CharField(blank=True, max_length=500, null=True)),
                ('Buy_week_two_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Buy_week_three', models.CharField(blank=True, max_length=500, null=True)),
                ('Buy_week_three_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Buy_week_four', models.CharField(blank=True, max_length=500, null=True)),
                ('Buy_week_four_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Progress_week_one', models.CharField(blank=True, max_length=500, null=True)),
                ('Progress_week_one_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Progress_week_two', models.CharField(blank=True, max_length=500, null=True)),
                ('Progress_week_two_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Progress_week_three', models.CharField(blank=True, max_length=500, null=True)),
                ('Progress_week_three_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Progress_week_four', models.CharField(blank=True, max_length=500, null=True)),
                ('Progress_week_four_chart', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('My_measurements_and_progress', models.CharField(blank=True, max_length=500, null=True)),
                ('The_summary_of_the_progression_curve', models.CharField(blank=True, max_length=500, null=True)),
                ('Meal_close_to_the_training_summary', models.CharField(blank=True, max_length=500, null=True)),
                ('Pre_post_recipe_data', models.CharField(blank=True, max_length=500, null=True)),
                ('In_Case_recipe_data', models.CharField(blank=True, max_length=500, null=True)),
                ('Meal_away_training_recipe_data', models.CharField(blank=True, max_length=500, null=True)),
                ('Dessert_recipe_data', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
