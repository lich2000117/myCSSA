# Generated by Django 2.1.7 on 2019-02-26 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthAPI', '0011_auto_20190218_0454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('activate_membership', 'Can activate new membership'),)},
        ),
    ]
