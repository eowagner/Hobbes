# Generated by Django 2.2.1 on 2019-05-08 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicgoods', '0008_remove_game_instance_time_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_instance',
            name='time_closed',
            field=models.DateTimeField(null=True),
        ),
    ]
