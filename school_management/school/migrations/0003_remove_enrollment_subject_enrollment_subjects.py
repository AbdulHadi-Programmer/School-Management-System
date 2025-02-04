# Generated by Django 5.1.2 on 2025-01-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_rename_class_schoolclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='subject',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='subjects',
            field=models.ManyToManyField(to='school.subject'),
        ),
    ]
