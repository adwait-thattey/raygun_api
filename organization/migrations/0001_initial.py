# Generated by Django 2.1.5 on 2020-07-23 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('administrators', models.ManyToManyField(blank=True, null=True, related_name='admin_orgnizations', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='creator_organization', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(blank=True, null=True, related_name='users_organizations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
