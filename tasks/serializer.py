from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.db.models import Q
from tasks.models import Employee, Task
from tasks.validators import TitleValidator
from rest_framework.serializers import UniqueTogetherValidator


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeActiveTasksSerializer(ModelSerializer):
    count_active_tasks = SerializerMethodField()
    tasks = SerializerMethodField()

    def get_count_active_tasks(self, employee):
        return Task.objects.filter(Q(employee=employee.id), Q(is_active=True)).count()

    def get_tasks(self, employee):
        tasks = Task.objects.filter(employee=employee.id)
        tasks_list = []
        for task in tasks:
            if task.is_active:
                tasks_list.append(task.title)
        return tasks_list

    class Meta:
        model = Employee
        fields = ("full_name", "tasks", "count_active_tasks")


class TaskSerializer(ModelSerializer):
    term_days = SerializerMethodField()

    def get_term_days(self, task):
        if task.end_date and task.start_date:
            return (task.end_date - task.start_date).days

    class Meta:
        model = Task
        fields = "__all__"
        validators = [
            TitleValidator(field="title"),
            UniqueTogetherValidator(fields=["title"], queryset=Task.objects.all())
        ]


class ImportantTaskSerializer(ModelSerializer):
    term_days = SerializerMethodField()
    employees = SerializerMethodField()
    parent_task_title = SerializerMethodField()

    def get_employees(self, task):
        employees_task = Task.objects.filter(id=task.id)
        employees_list = []
        for task in employees_task:
            employees_list.append(task.employee.full_name)
        return employees_list

    def get_term_days(self, task):
        if task.end_date and task.start_date:
            return (task.end_date - task.start_date).days

    def get_parent_task_title(self, task):
        return task.parent_task.title

    class Meta:
        model = Task
        fields = (
            "title",
            "parent_task_title",
            "start_date",
            "end_date",
            "comments",
            "term_days",
            "employees",
        )
