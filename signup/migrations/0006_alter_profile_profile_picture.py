# Generated by Django 5.2 on 2025-07-25 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_alter_profile_telephone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pictures/'),
        ),
    ]
