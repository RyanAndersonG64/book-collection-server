# Generated by Django 5.0.6 on 2024-05-30 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0003_rename_first_name_author_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='reader',
            new_name='readers',
        ),
    ]
