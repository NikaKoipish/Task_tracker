from rest_framework.serializers import ModelSerializer

from tasks.models import Employee, Task


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ["full_name", "position"]


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "title",
            "parent_task",
            "employee",
            "start_date",
            "end_date",
            "comments",
        ]
