# Generated by Django 4.2.4 on 2023-09-19 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0004_clientprofile_building_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='inspector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
