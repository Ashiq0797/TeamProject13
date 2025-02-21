# Generated by Django 5.0.1 on 2024-02-08 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientInclusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantityGrams', models.IntegerField()),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.menuitem')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ingredient')),
            ],
        ),
    ]
