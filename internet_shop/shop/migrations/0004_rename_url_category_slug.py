# Generated by Django 4.0.4 on 2022-05-05 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_basket_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='url',
            new_name='slug',
        ),
    ]