# Generated by Django 2.2 on 2019-04-16 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlexForm', '0005_auto_20190414_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexformfield',
            name='is_required',
            field=models.BooleanField(default=False, verbose_name='是否为必填项？'),
        ),
    ]
