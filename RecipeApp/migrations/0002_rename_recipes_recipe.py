# Generated by Django 5.0 on 2023-12-28 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipes',
            new_name='Recipe',
        ),
    ]
