# Generated by Django 4.0.4 on 2022-05-31 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_alter_class_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='date_create',
            field=models.DateField(max_length=15),
        ),
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(max_length=5),
        ),
    ]
