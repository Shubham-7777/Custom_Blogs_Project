# Generated by Django 3.0.2 on 2020-08-10 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0002_auto_20200730_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='user_id',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
