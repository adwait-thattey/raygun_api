# Generated by Django 2.1.5 on 2020-07-24 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs_manager', '0006_auto_20200724_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinteraction',
            name='element',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userinteraction',
            name='elementId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userinteraction',
            name='innerText',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinteraction',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinteraction',
            name='timestamp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
