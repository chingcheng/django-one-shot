from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm

# Create your views here.
def todo_list_list(request):
    todo_lists = TodoList.objects.all()
    context = {
        "todo_lists": todo_lists,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todos/detail.html", context)


def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            list = form.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoListForm()

    context = {
        "form": form,
    }

    return render(request, "todos/create.html", context)


def todo_list_update(request, id):
    list = TodoList.objects.get(id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=list)
        if form.is_valid():
            list = form.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoListForm(instance=list)
    context = {
        "form": form,
    }

    return render(request, "todos/edit.html", context)


def todo_list_delete(request, id):
    list = TodoList.objects.get(id=id)
    if request.method == "POST":
        list.delete()
        return redirect("todo_list_list")

    return render(request, "todos/delete.html")
