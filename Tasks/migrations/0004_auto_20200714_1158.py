# Generated by Django 3.0.7 on 2020-07-14 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0003_auto_20200714_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tasks',
            field=models.TextField(max_length=100),
        ),
    ]
