from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.task_list, name='task-list'),
    path('add/', views.add_task, name='add-task'),
]
