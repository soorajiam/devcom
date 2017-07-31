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
