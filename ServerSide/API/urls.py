from django.urls import path, include
from API.views import *

urlpatterns = [
    path('ToDo', ToDoListView.as_view(), name='index'),
    path('ToDo/<int:todo_id>', ToDoView.as_view(), name='detail')
]
