from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from myapp.forms import CreateNewTask,CreateNewProject
from .models import Project, Task


# Create your views here.
def index(request):
    title = 'Welcome to BetaWork'
    return render(request, 'index.html', {
        'title': title
    })

def hello(request,username):
    print('username')
    return HttpResponse('Hello %s</h2>' %username)

def about(request):
    username = 'fazt'
    return render(request,'about.html',{
        'username': username
    })

def projects(request):
    #projects1 = list(Project.objects.values())
    #return JsonResponse(projects1, safe=False)
    projects1 = Project.objects.all()
    return render(request,'projects/projects.html',{
        'projects':projects1
    })
def tasks(request):
    
    #task = get_object_or_404(Task, id = id)
    #return HttpResponse('task: %s'%task.title)
    task1 = Task.objects.all()
    return render(request,'tasks/tasks.html',{
        'tasks' : task1
    })

def create_task(request):
    
    if request.method == 'GET':
        return render(request,'tasks/create_task.html',{
            'form': CreateNewTask()
    })
    else:
        Task.objects.create(title=request.POST['title'],
        description=request.POST['description'],project_id=1)
        return redirect('tasks')

def create_project(request):
    
    if request.method == 'GET':
        return render(request,'projects/create_project.html',{
            'form': CreateNewProject()
        })
    else:
        project1 = Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def project_detail(request,id):
    project1 = get_object_or_404(Project,id = id)
    tasks1 = Task.objects.filter(project_id = id)
    return render(request,'projects/detail.html',{
        'project': project1,
        'tasks' : tasks1
    })