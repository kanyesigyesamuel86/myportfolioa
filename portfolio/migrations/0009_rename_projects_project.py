# Generated by Django 5.0.1 on 2024-02-01 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_profile_project'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
