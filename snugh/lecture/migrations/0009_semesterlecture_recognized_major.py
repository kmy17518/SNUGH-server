# Generated by Django 3.1 on 2021-03-27 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210319_1716'),
        ('lecture', '0008_auto_20210319_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='semesterlecture',
            name='recognized_major',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='semesterlecture', to='user.major'),
        ),
    ]
