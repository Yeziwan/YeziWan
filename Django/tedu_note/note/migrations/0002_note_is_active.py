# Generated by Django 4.0.3 on 2022-05-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='是否活跃'),
        ),
    ]