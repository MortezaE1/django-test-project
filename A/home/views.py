from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm, TodoUpdateForm


def home(request):
    all_todo = Todo.objects.all()
    return render(request, 'home.html', {'todos': all_todo})


def detail(request, todo_id):
    post = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {"todo": post})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'Todo deleted successfully.', 'success')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
            messages.success(request, 'Todo created successfully.')
            return redirect('home')
    else:
        form = TodoCreateForm
    return render(request, 'create.html', {'form': form})


def update(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo updated successfully...', 'success')
            return redirect('detail', todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form': form})
