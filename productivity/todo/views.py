from django.shortcuts import render
from .models import task
# Create your views here.

def index(request):
    tasks = task.objects.all()
    context = {
        'tasks' : tasks,
    }
    return render(request, 'todo/index.html', context)