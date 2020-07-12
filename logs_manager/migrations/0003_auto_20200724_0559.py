# Generated by Django 2.1.5 on 2020-07-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs_manager', '0002_auto_20200724_0526'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loginstance',
            options={'ordering': ('log_id', '-timestamp')},
        ),
        migrations.AlterField(
            model_name='logobject',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]