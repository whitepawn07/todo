# Generated by Django 3.0 on 2019-12-16 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_list_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='list',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Category'),
        ),
    ]
