# Generated by Django 4.0.4 on 2022-05-27 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_managers_remove_user_date_joined_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_superuser',
        ),
    ]
