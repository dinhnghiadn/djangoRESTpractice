# Generated by Django 4.0.4 on 2022-05-27 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['name']},
        ),
    ]