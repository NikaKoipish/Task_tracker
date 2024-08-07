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
    STATUS_DONE = "done"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_NOT_STARTED = "not_started"
    STATUS = [
        (STATUS_DONE, "Выполнено"),
        (STATUS_IN_PROGRESS, "В процессе выполнения"),
        (STATUS_NOT_STARTED, "Не приступал к выполнению"),
    ]

    title = models.CharField(max_length=255, verbose_name="Название задачи")
    parent_task = models.ForeignKey(
        "self", on_delete=models.CASCADE, **NULLABLE, verbose_name="Родительская задача"
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name="Иcполнитель"
    )
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    status = models.CharField(
        max_length=20, choices=STATUS, default=STATUS_NOT_STARTED, verbose_name="Статус"
    )
    comments = models.TextField(verbose_name="Комментарии к задаче", **NULLABLE)
    owner = models.TextField(verbose_name="создатель", **NULLABLE)
    is_active = models.BooleanField(
        default=True, verbose_name="Признак активности задачи"
    )
    is_important = models.BooleanField(
        default=False, verbose_name="Признак важности задачи"
    )

    def __str__(self):
        return f"{self.title}: {self.status}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
