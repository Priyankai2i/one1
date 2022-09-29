# Generated by Django 4.1 on 2022-09-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_player_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='question_bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Match', models.CharField(max_length=250)),
                ('Questions', models.CharField(max_length=250)),
                ('option_A', models.CharField(max_length=250)),
                ('option_B', models.CharField(max_length=250)),
                ('option_C', models.CharField(max_length=250)),
                ('option_D', models.CharField(max_length=250)),
                ('Right_Answer', models.CharField(max_length=250)),
                ('quiz_fact', models.CharField(max_length=250)),
                ('image', models.ImageField(default='logo.png', upload_to='')),
            ],
        ),
    ]
