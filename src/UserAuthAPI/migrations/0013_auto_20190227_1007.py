# Generated by Django 2.1.7 on 2019-02-27 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthAPI', '0012_auto_20190226_2243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('activate_membership', 'Can activate new membership'), ('change_indentity_data', 'Can change identity_data'))},
        ),
    ]