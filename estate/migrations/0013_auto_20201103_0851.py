# Generated by Django 3.1.2 on 2020-11-03 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0012_business_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
