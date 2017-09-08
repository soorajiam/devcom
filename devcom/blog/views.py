from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render,redirect
from User.models import User,Dp
from .models import Post
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def me(request):
    try:
        id = request.session['logid']
    except Exception:
        return render(request,'login.html',{'error' : 'Please Login to Continue'  })
    usrs=User.objects.all().filter(uid=id)
    for u in usrs:
        a=0
    posts=Post.objects.all().filter(uid=u)


    return render(request,'myblog.html',{'posts' : posts})

def new(request):
    try:
        id = request.session['logid']
    except Exception:
        return render(request,'login.html',{'error' : 'Please Login to Continue'  })
    usrs=User.objects.all().filter(uid=id)
    for u in usrs:
        a=0
    return render(request,'newpost.html')

def newprocess(request):
    try:
        id = request.session['logid']
    except Exception:
        return render(request,'login.html',{'error' : 'Please Login to Continue'  })
    usrs=User.objects.all().filter(uid=id)
    for u in usrs:
        a=0
    title=request.POST.get('title','')
    content=request.POST.get('content','')
    p=Post(title=title,content=content,uid=u,date=timezone.now())
    p.save()
    return redirect('/blog/me')

class edit(UpdateView):
    model=Post
    fields=['title','topic','content','cover']
    success_url='/blog/me'


class PostDelete (DeleteView):
    model=Post
    success_url='/blog/me'

def blog(request):
    posts=Post.objects.all().order_by('-postid')
    users=User.objects.all()
    return render(request,'blog.html',{'posts':posts,'users':users})

def view(request,pk):
    posts=Post.objects.all().filter(postid=pk)
    for p in posts:
        a=0
    return render(request,'post.html',{'p':p})

class Profile(CreateView):
    model= Dp
    fields=['dp','user']
    success_url='/blog'
