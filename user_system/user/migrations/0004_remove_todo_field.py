# Generated by Django 3.0.8 on 2020-08-27 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_todo_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='field',
        ),
    ]