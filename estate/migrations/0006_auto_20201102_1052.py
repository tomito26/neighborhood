# Generated by Django 3.1.2 on 2020-11-02 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0005_auto_20201102_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighborhood',
            old_name='neigborhood_name',
            new_name='neighborhood_name',
        ),
    ]
