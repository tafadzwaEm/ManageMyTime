from django.urls import path
from .views import (
                    TodoView, CreateTodoView, 
                    UpdateTodoView, DeleteTodoView,
                    CreateUpcomingView, UpdateUpcomingView,
                    DeleteUpcomingView, Register, 
                    )

urlpatterns = [
    path('',TodoView.as_view(),name='home'),
    path('register/',Register,name='register'),
    path('todays-tasks/addtask/',CreateTodoView.as_view(),name='add-task'),
    path('todays-tasks/<int:pk>/update/',UpdateTodoView.as_view(),name='edit-task'),
    path('todays-tasks/<int:pk>/remove/',DeleteTodoView.as_view(),name='remove-task'),

    path('upcoming/addevent/',CreateUpcomingView.as_view(),name='add-event'),
    path('upcoming/<int:pk>/update/',UpdateUpcomingView.as_view(),name='edit-event'),
    path('upcoming/<int:pk>/remove/',DeleteUpcomingView.as_view(),name='remove-event'),
]