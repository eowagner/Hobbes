# Generated by Django 2.2.1 on 2019-05-05 02:41

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicgoods', '0002_auto_20190504_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_instance',
            name='pot_multiplier',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
    ]
