# Generated by Django 4.2.6 on 2023-11-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypolls', '0002_pollchoice_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='winVote',
            field=models.IntegerField(default=50),
        ),
    ]
