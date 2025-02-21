# Generated by Django 5.0.1 on 2024-03-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_menuitem_category_alter_menuitem_spice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('drinks', 'Drink'), ('mains', 'Main'), ('desserts', 'Dessert'), ('starters', 'Starter')], default='mains', max_length=200),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='spice',
            field=models.CharField(choices=[('mild', 'Mild'), ('atomic', 'Atomic'), ('hot', 'Hot'), ('spiceless', 'Spiceless')], default='spiceless', max_length=200),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('CKG', 'Cooking'), ('REC', 'Received'), ('COM', 'Completed'), ('RTC', 'Ready to collect')], max_length=3),
        ),
    ]
