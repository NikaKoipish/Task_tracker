# Generated by Django 5.0.7 on 2024-07-17 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=150, verbose_name="ФИО")),
                (
                    "position",
                    models.CharField(max_length=100, verbose_name="Должность"),
                ),
                (
                    "vacation_status",
                    models.BooleanField(
                        default=False,
                        verbose_name="Статус нахождения в отпуске/на выходном/ на больничном",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сотрудник",
                "verbose_name_plural": "Сотрудники",
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Название задачи"),
                ),
                ("start_date", models.DateField(verbose_name="Дата начала")),
                ("end_date", models.DateField(verbose_name="Дата окончания")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("done", "Выполнено"),
                            ("in_progress", "В процессе выполнения"),
                            ("not_started", "Не приступал к выполнению"),
                        ],
                        default="not_started",
                        max_length=20,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tasks.employee",
                        verbose_name="Иполнитель",
                    ),
                ),
                (
                    "parent_task",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tasks.task",
                        verbose_name="Родительская задача",
                    ),
                ),
            ],
            options={
                "verbose_name": "Задача",
                "verbose_name_plural": "Задачи",
            },
        ),
    ]
