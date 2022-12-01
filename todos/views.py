from django.shortcuts import render
from todos.models import TodoList

# Create your views here.
def todo_list_list(request):
    todos = TodoList.objects.all()
    context = {
        "todo_list": todos,
    }
    return render(request, "todos/list.html", context)
