# Generated by Django 3.0.1 on 2021-03-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210320_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='users_profiles/default-user-img-768x768.jpg', upload_to='users_profiles/'),
        ),
    ]