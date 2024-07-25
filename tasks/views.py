from django.db.models import Q
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from tasks.models import Employee, Task
from tasks.serializer import EmployeeSerializer, TaskSerializer, ImportantTaskSerializer


class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        task.owner = self.request.user
        task.save()


class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        self.queryset = Task.objects.filter(
            Q(status="not_started")
        )
        return self.queryset


class ImportantTaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = ImportantTaskSerializer


class TaskRetrieveAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (
        OrderingFilter,
    )
    ordering_fields = "__all__" # как сделать кастомное поле частью сортировки?
