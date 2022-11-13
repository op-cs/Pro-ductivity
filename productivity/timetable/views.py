from django.shortcuts import render
from .models import time_task

# Create your views here.
def index(request):
    tasks = time_task.objects.all()
    if request.method == 'POST':
        day_chosen = request.POST['select']
    else: 
        day_chosen = 'All'
    context = {
        'tasks' : tasks,
        'day_chosen' : day_chosen,
    }
    return render(request, 'timetable/index.html', context)