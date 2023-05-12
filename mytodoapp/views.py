from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    todos = Task.objects.all()

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
    }
    return render(request, 'index.html',context)

def about(request):
    return HttpResponse("<h1>About pge</h1>")