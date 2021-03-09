# Generated by Django 3.1 on 2021-03-09 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lecture', '0004_semester_is_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='lecture_id',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='plan',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plan', to=settings.AUTH_USER_MODEL),
        ),
    ]