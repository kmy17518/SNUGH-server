# Generated by Django 3.1 on 2021-02-16 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0003_remove_plan_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]