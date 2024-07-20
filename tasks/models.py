from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}


class Employee(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="ФИО")
    position = models.CharField(max_length=100, verbose_name="Должность")
    vacation_status = models.BooleanField(
        default=False,
        verbose_name="Статус нахождения в отпуске/на выходном/ на больничном",
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Task(models.Model):
    STATUS = [
        ("done", "Выполнено"),
        ("in_progress", "В процессе выполнения"),
        ("not_started", "Не приступал к выполнению"),
    ]
    title = models.CharField(max_length=255, verbose_name="Название задачи")
    parent_task = models.ForeignKey(
        "self", on_delete=models.CASCADE, **NULLABLE, verbose_name="Родительская задача"
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name="Иполнитель"
    )
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    status = models.CharField(
        max_length=20, choices=STATUS, default="not_started", verbose_name="Статус"
    )
    comments = models.TextField(verbose_name="Комментарии к задаче", **NULLABLE)
    owner = models.ForeignKey(
        User, verbose_name="создатель", on_delete=models.CASCADE, **NULLABLE
    )

    def __str__(self):
        return f"{self.title}: {self.status}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
