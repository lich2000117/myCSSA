# Generated by Django 2.2.3 on 2019-07-16 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PrizeAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prize',
            name='prize_UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
