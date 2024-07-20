from rest_framework.routers import DefaultRouter
from django.urls import path
from tasks.apps import TasksConfig
from tasks.views import (
    EmployeeViewSet,
    TaskListAPIView,
    TaskCreateAPIView,
    TaskRetrieveAPIView,
    TaskUpdateAPIView,
    TaskDestroyAPIView,
)

app_name = TasksConfig.name

router = DefaultRouter()
router.register(r"employee", EmployeeViewSet, basename="employee")

urlpatterns = [
    path("", TaskListAPIView.as_view(), name="task_list"),
    path("create/", TaskCreateAPIView.as_view(), name="task_create"),
    path("<int:pk>/", TaskRetrieveAPIView.as_view(), name="task_retrieve"),
    path("<int:pk>/update/", TaskUpdateAPIView.as_view(), name="task_update"),
    path("<int:pk>/delete/", TaskDestroyAPIView.as_view(), name="task_delete"),
] + router.urls
