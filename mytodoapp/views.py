from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

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

def update(request, pk):
    todoappvalue = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = todoappvalue)
    
    else:
        forms = TaskForm(instance = todoappvalue)

    context = {
        "form":forms
    }
    return render(request,'update.html', context)