# Generated by Django 2.1.7 on 2019-02-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventAPI', '0012_eventattendentinfoform'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendevent',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attendevent',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attendevent',
            name='token',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='attendevent',
            name='token_used',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='WechatArticleUrl',
            field=models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='微信公众号文章链接'),
        ),
    ]
