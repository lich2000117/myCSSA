# Generated by Django 2.2.1 on 2019-05-09 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinanceAPI', '0002_auto_20181228_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banktransferrecipient',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='UserAuthAPI.UserProfile'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='uploader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='UserAuthAPI.UserProfile'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='related_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='UserAuthAPI.UserProfile'),
        ),
        migrations.AlterField(
            model_name='transactionreview',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='UserAuthAPI.UserProfile'),
        ),
    ]
