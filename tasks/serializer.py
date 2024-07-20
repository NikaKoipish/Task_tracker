from tasks.models import Employee, Task


class EmployeeSerializer:
    class Meta:
        model = Employee
        fields = ['full_name', 'position']


class TaskSerializer:
    class Meta:
        model = Task
        fields = ['title', 'parent_task', 'employee', 'start_date', 'end_date', 'comments']

