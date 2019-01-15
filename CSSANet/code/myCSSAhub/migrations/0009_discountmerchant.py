# Generated by Django 2.1.3 on 2019-01-14 08:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myCSSAhub', '0008_emaildb'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountMerchant',
            fields=[
                ('merchant_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('merchant_name', models.CharField(max_length=200, null=True, verbose_name='商家名')),
                ('merchant_description', models.CharField(max_length=200, null=True, verbose_name='商家介绍')),
                ('merchant_phone', models.CharField(max_length=200, null=True, verbose_name='联系电话')),
                ('merchant_address', models.CharField(max_length=200, null=True, verbose_name='商家地址')),
                ('merchant_link', models.CharField(max_length=200, null=True, verbose_name='商家网站')),
                ('merchant_add_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='商户加入时间')),
                ('merchant_image', models.ImageField(default='img/merchants/noneImg.jpg', upload_to='img/merchants/')),
            ],
        ),
    ]
