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
        #fields = "__all__"
        fields = ("full_name", "tasks", "count_active_tasks")


class TaskSerializer(ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Task
        fields = "__all__"

