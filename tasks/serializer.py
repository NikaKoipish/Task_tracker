from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.db.models import Q
from tasks.models import Employee, Task


class EmployeeSerializer(ModelSerializer):
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


class ImportantTaskSerializer(ModelSerializer):
    term_days = SerializerMethodField()
    employees = SerializerMethodField()

    def get_employees(self, task):
        employees_task = Task.objects.filter(id=task.id)
        employees_list = []
        for task in employees_task:
            employees_list.append(task.employee.full_name)
        return employees_list

    def get_term_days(self, task):
        if task.end_date and task.start_date:
            return (task.end_date - task.start_date).days

    class Meta:
        model = Task
        fields = ("title", "term_days", "employees",)
