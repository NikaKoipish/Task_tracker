# Generated by Django 5.0.7 on 2024-07-23 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_task_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="is_active",
            field=models.BooleanField(
                default=True, verbose_name="Признак активности задачи"
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="employee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="tasks.employee",
                verbose_name="Иcполнитель",
            ),
        ),
    ]
