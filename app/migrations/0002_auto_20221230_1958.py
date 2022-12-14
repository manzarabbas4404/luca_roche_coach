# Generated by Django 3.2.16 on 2022-12-30 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_table',
            old_name='Buy_week_four',
            new_name='Buy_week_summary',
        ),
        migrations.RenameField(
            model_name='user_table',
            old_name='Buy_week_one',
            new_name='Food_Plan_Week_Summary',
        ),
        migrations.RenameField(
            model_name='user_table',
            old_name='Buy_week_three',
            new_name='Progress_Week_summary',
        ),
        migrations.RenameField(
            model_name='user_table',
            old_name='Buy_week_two',
            new_name='Training_Plan_Week_Summary',
        ),
        migrations.RemoveField(
            model_name='user_table',
            name='Food_Plan_Summary_week_four',
        ),
        migrations.RemoveField(
            model_name='user_table',
            name='Food_Plan_Summary_week_one',
        ),
        migrations.RemoveField(
            model_name='user_table',
            name='Food_Plan_Summary_week_three',
        ),
        migrations.RemoveField(
            model_name='user_table',
            name='Food_Plan_Summary_week_two',
        ),
        migrations.RemoveField(
            model_name='user_table',
            name='Progress_week_four',
        ),
        migrations.RemoveField(
            model_name='user_table',
            name='Progress_week_one',
        ),
        migrations.RemoveField(
            model_name='user_table',
            name='Progress_week_three',
        ),
        migrations.RemoveField(
            model_name='user_table',
            name='Progress_week_two',
        ),
        migrations.RemoveField(
            model_name='user_table',
            name='Training_Plan_Summary_week_four',
        ),
        migrations.RemoveField(
            model_name='user_table',
            name='Training_Plan_Summary_week_one',
        ),
        migrations.RemoveField(
            model_name='user_table',
            name='Training_Plan_Summary_week_three',
        ),
        migrations.RemoveField(
            model_name='user_table',
            name='Training_Plan_Summary_week_two',
        ),
    ]
