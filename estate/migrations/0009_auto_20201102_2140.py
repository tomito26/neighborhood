# Generated by Django 3.1.2 on 2020-11-02 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0008_auto_20201102_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='business_name',
            new_name='name',
        ),
    ]
