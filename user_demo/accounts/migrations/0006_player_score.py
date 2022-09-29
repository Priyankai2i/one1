# Generated by Django 4.1 on 2022-09-26 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_gu_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='player_score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.CharField(default='player_id', max_length=10)),
                ('myscr', models.IntegerField(default=0)),
                ('season_gameid', models.CharField(default='gameid', max_length=10)),
                ('total_score', models.IntegerField(default=0)),
                ('played_dt', models.DateField(verbose_name=datetime.date(2022, 9, 26))),
                ('player_groupid', models.CharField(default='group_id', max_length=10)),
            ],
        ),
    ]