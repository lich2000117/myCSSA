# Generated by Django 2.2.3 on 2019-07-16 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PrizeAPI', '0002_auto_20190716_0721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prize',
            old_name='prize_UserId',
            new_name='prize_userId',
        ),
    ]
