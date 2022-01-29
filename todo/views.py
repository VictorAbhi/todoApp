from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem


def home(request):
    return render(request, 'home.html')


def todo(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html', {'all_items': all_todo_items})


def AddTodoView(request):
    todo_item = request.POST['content']
    new_item = TodoListItem(content=todo_item)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')


def deleteTodoView(request, i):
    todo_item = TodoListItem.objects.get(id=i)
    todo_item.delete()
    return HttpResponseRedirect('/todoapp/')
