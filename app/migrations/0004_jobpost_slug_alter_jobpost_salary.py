# Generated by Django 5.0.7 on 2024-09-04 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_jobpost_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
