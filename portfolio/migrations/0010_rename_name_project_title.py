# Generated by Django 5.0.1 on 2024-02-01 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_rename_projects_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='title',
        ),
    ]