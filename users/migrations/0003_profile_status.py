# Generated by Django 3.0.1 on 2021-03-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210319_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.TextField(max_length=150, null=True),
        ),
    ]