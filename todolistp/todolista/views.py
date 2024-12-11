from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from todolista.models import *
# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def mark_as_read(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('/')

def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST.get('description', '')
        Task.objects.create(title=title, description=description)
        return redirect('home')
    return render(request, 'addtask.html')

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('home')
    return render(request, 'updatetask.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')

