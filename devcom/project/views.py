from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render,redirect
from User.models import User,Dp
from .models import Project,Team,Stage
from blog.models import Post
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView



def team(request):
    users=User.objects.all().filter(isteam=2)
    return render(request,'team.html',{'users':users})

def teamprocess(request,p,u):

    try:
        id = request.session['logid']
    except Exception:
        return render(request,'login.html',{'error' : 'Please Login to Continue'  })
    usrs=User.objects.all().filter(uid=id)
    for us in usrs:
        a=0
    project=Project.objects.all().filter(projectid=p)
    for pr in project:
        a=0
    h=Team(project=pr,user=us,duty='Joined')
    h.save()

    return redirect('/team/projects')

def addprocess(request):

    try:
        id = request.session['logid']
    except Exception:
        return render(request,'login.html',{'error' : 'Please Login to Continue'  })
    usrs=User.objects.all().filter(uid=id)
    for u in usrs:
        a=0
    projectname=request.POST.get('projectname','')
    tools=request.POST.get('tools','')
    github=request.POST.get('github','')
    desc=request.POST.get('desc','')
    p=Project(projectname=projectname,tools=tools,github=github,desc=desc,mentor=u)
    if(projectname!=''):
        p.save()
    return redirect('/team/projects')

def addnew(request):
    users=User.objects.all().filter(isteam=2)
    return render(request,'projectadd.html')
# Create your views here.
def projects(request):
    users=User.objects.all().filter(isteam=2)
    project=Project.objects.all()
    team=Team.objects.all()
    return render(request,'projects.html',{'project':project,'team':team})

def projectview(request,pk):
    users=User.objects.all().filter(isteam=2)
    project=Project.objects.all().filter(projectid=pk)
    for p in project:
        a=0
    team=Team.objects.all()
    stage=Stage.objects.all().filter(project=p).order_by('-stageid')
    return render(request,'projectview.html',{'p':p,'team':team,'stage':stage})

class projectedit(UpdateView):
    model=Project
    fields=['projectname','tools','github','desc','cover']
    success_url='/team/projects'


def addupdate(request,pk):
    ide=request.session['logid']
    users=User.objects.all()
    us=User.objects.all().filter(uid=ide)
    for u in us:
        a=0

    ps=Project.objects.all().filter(projectid=pk)
    for p in ps:
        s=0
    projects=Project.objects.all()
    context={'u':u , 'p' : p , 'projects' : projects , 'users' : users}
    return render(request,'addupdate.html',{'c':context})

def updateprocess(request):
    project = Project()
    user=User()
    uid=request.POST.get('user','')
    pid=request.POST.get('project','')
    date=request.POST.get('date','')
    update=request.POST.get('update','')
    pro=Project.objects.all().filter(projectid=pid)
    for project in pro:
        a=0
    us = User.objects.all().filter(uid=uid)
    for user in us:
        a=0
    if(uid == '' or update=='' or pid == '' ):
        return redirect('/blog')
    p=Stage(project=project,user=user,info=update,date=date)
    p.save()
    return redirect('/team/projects/'+pid)
