# Generated by Django 3.0 on 2019-12-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
