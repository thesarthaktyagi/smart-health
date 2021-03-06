# Generated by Django 3.1.5 on 2021-01-15 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='about',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='department',
            name='image',
            field=models.ImageField(blank=True, upload_to='hospital/departments/'),
        ),
    ]
