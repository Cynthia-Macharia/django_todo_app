# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('update/<int:todo_id>/', views.update_todo, name='update_todo'),  # URL for updating
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),  # Delete URL
]

