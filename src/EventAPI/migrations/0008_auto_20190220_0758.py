# Generated by Django 2.1.7 on 2019-02-20 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventAPI', '0007_auto_20190220_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='mainVisual',
            field=models.ImageField(default=None, null=True, upload_to='uploads/usrImage/eventMainVisual', verbose_name='主视觉图'),
        ),
    ]
