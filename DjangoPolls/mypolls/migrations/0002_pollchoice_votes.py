# Generated by Django 4.2.6 on 2023-10-23 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypolls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollchoice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]