from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todoapp/', views.todo, name='todoApp'),
    path('addTodoItem/', views.AddTodoView),
    path('deleteTodoItem/<int:i>/', views.deleteTodoView),
]

