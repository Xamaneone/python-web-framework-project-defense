# Generated by Django 3.2.6 on 2021-08-08 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_profile_is_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='display_name',
            field=models.CharField(max_length=150),
        ),
    ]
