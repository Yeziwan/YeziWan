# Generated by Django 4.0.3 on 2022-03-24 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name_plural': '笔记'},
        ),
        migrations.AlterModelTable(
            name='note',
            table='note',
        ),
    ]
