# Generated by Django 2.2.4 on 2019-08-22 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FlexForm', '0007_auto_20190509_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexformdata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]