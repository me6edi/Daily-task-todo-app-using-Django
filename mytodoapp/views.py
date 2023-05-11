from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.
def index(request):
    todos = Task.objects.all()
    context = {
        'todo': todos
    }
    return render(request, 'index.html',context)

def about(request):
    return HttpResponse("<h1>About pge</h1>")