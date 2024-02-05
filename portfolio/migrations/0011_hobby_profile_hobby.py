# Generated by Django 5.0.1 on 2024-02-03 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_rename_name_project_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='hobby',
            field=models.ManyToManyField(to='portfolio.hobby'),
        ),
    ]