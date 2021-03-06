# Generated by Django 2.2.1 on 2019-05-03 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game_Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_name', models.CharField(max_length=200)),
                ('pot_multiplier', models.DecimalField(decimal_places=2, max_digits=5)),
                ('endowment', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_contribution', models.DecimalField(decimal_places=2, max_digits=5)),
                ('expected_n', models.IntegerField(default=35)),
                ('password_protected', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=200)),
                ('time_opened', models.DateTimeField()),
                ('time_closed', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Game_Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribution', models.DecimalField(decimal_places=2, max_digits=5)),
                ('name', models.CharField(max_length=200)),
                ('eid', models.CharField(max_length=200)),
                ('pseudonym', models.CharField(max_length=200)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicgoods.Game_Instance')),
            ],
        ),
    ]
