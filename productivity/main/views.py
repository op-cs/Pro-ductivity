from django.shortcuts import render
from timetable.models import time_task
from todo.models import task
# Create your views here.

def index(request):
    time_tasks = time_task.objects.all()
    tasks = task.objects.all()
    context = {
        'time_tasks' : time_tasks,
        'tasks' : tasks,
    }
    return render(request, 'main/index.html', context)