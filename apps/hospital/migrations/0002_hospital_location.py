# Generated by Django 3.1.5 on 2021-01-15 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='location',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]