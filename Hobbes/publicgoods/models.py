from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

MAX_LEN = 100

class Game_Instance(models.Model):
    instance_name = models.CharField(max_length=MAX_LEN)
    pot_multiplier = models.DecimalField(max_digits=5, decimal_places=2, default=2, validators=[MinValueValidator(Decimal('0.00'))])
    endowment = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    max_contribution = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    expected_n = models.IntegerField(default=35)
    password_protected = models.BooleanField(default=True)
    instructor_password = models.CharField(max_length=MAX_LEN, default="")
    user_keyword = models.CharField(max_length=MAX_LEN, default="")
    time_opened = models.DateTimeField()
    time_closed = models.DateTimeField(null=True)
    available = models.BooleanField(default=True)

class Game_Response(models.Model):
    game = models.ForeignKey(Game_Instance, on_delete=models.CASCADE)
    contribution = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    name = models.CharField(max_length=MAX_LEN)
    eid = models.CharField(max_length=MAX_LEN)
    pseudonym = models.CharField(max_length=MAX_LEN)


