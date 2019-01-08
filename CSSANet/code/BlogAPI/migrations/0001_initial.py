# Generated by Django 2.1.3 on 2019-01-03 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogContent',
            fields=[
                ('blogContentId', models.AutoField(primary_key=True, serialize=False)),
                ('blogMainContent', models.TextField()),
                ('writtenDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogDescription',
            fields=[
                ('blogId', models.AutoField(primary_key=True, serialize=False)),
                ('blogTitle', models.CharField(max_length=100)),
                ('blogReads', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogInTag',
            fields=[
                ('blogTagId', models.AutoField(primary_key=True, serialize=False)),
                ('blogId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogAPI.BlogDescription')),
            ],
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('tagId', models.AutoField(primary_key=True, serialize=False)),
                ('tagName', models.CharField(max_length=18)),
                ('tagCreateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogWrittenBy',
            fields=[
                ('blogCreatedId', models.AutoField(primary_key=True, serialize=False)),
                ('blogContentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogAPI.BlogContent')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blogintag',
            name='tagId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogAPI.BlogTag'),
        ),
        migrations.AddField(
            model_name='blogcontent',
            name='blogId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogAPI.BlogDescription'),
        ),
    ]
