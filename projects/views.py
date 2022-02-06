from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from .utils import searchProjects,paginateProjects
from .models import Project,Tag
from .forms import ProjectForm,ReviewForm
from django.contrib.auth.decorators import login_required
# Create your views here.



def projects(request):
    projects,search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request,projects,2)


    
    context = {'projects': projects,'search_query':search_query,'custom_range':custom_range}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        
        projectObj.getVoteCount

        messages.success(request,'Your Review was successfully submitted')
        return redirect('project', pk=projectObj.id)
        

    return render(request, 'projects/single-project.html', {'project': projectObj,'form':form})

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm() 

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES)    
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')


    context = {'form' :form}
    return render(request, 'projects/projects-form.html',context)

@login_required(login_url="login")
def updateProject(request,pk):
    
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project) 


    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()

        form = ProjectForm(request.POST,request.FILES,instance=project)    
        if form.is_valid():
            form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')


    context = {'form' :form,'project':project}
    return render(request, 'projects/projects-form.html',context)

@login_required(login_url="login")
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
            project.delete()
            return redirect('projects')
    context = {'object' :project}
    return render(request, 'delete_template.html',context)


@login_required(login_url="login")
def createSkill(request):
    context = {}
    return render(request, 'users/skill_form.html',context)
