from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('create/', views.create, name="create"),
    path('task-list/', views.task_list, name="task-list"),
    path('task/<str:id>/', views.task_detail, name="detail"),
    path('delete/<str:id>/', views.deleteTask, name="delete"),
    path('edit/<str:id>/', views.updateTask, name="edit"),
    path('login/', obtain_auth_token, name='login'),
    path('register/', views.register, name='register'),
]