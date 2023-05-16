from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm,UpdateTaskForm

# Create your views here.
def index(request):
    todos = Task.objects.all()

    count_todos = todos.count()

    completed_todo = Task.objects.filter(complete=True)
    count_completed_todo = completed_todo.count()

    count_uncompleted_todo = count_todos - count_completed_todo


    if request.method == "POST":
        forms = TaskForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    else:
        forms = TaskForm()

    context = {
        'todo': todos,
        'form' : forms,
        'count': count_todos,
        'completed_todo': count_completed_todo,
        'uncompleted_todo': count_uncompleted_todo,
        
    }
    return render(request, 'index.html',context)

def update(request, id):
    todoappvalue = Task.objects.get(pk = id)

    if request.method == 'POST':
        forms = UpdateTaskForm(request.POST, instance = todoappvalue)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    else:
        forms = UpdateTaskForm(instance = todoappvalue)

    context = {
        "form":forms
    }
    return render(request,'update.html', context)

def delete(request, id):
    dailytasktodo = Task.objects.get(pk=id)
    if request.method == 'POST':
        dailytasktodo.delete()
        return redirect('/')
    return render(request,'delete.html')