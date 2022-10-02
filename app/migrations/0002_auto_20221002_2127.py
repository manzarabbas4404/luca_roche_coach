# Generated by Django 3.1.5 on 2022-10-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=50)),
                ('file1', models.ImageField(upload_to='')),
                ('file2', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]