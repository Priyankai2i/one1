# Generated by Django 4.1 on 2022-09-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ques_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qid', models.CharField(max_length=10)),
                ('ques', models.CharField(max_length=250)),
            ],
        ),
    ]
