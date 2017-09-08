from django.shortcuts import render,redirect
from .models import User,Dp
from blog.models import Post
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView



def home(request):
	return render(request, 'index.html' )
def signup(request):
	return render(request, 'signup.html' )


def login(request):
	return render(request, 'login.html' )
# Create your views here.

def signupprocess(request):
    name=request.POST.get('name','')
    username=request.POST.get('username','')
    email=request.POST.get('email','')
    mobile=request.POST.get('mobile','')
    clas=request.POST.get('class','')
    year=request.POST.get('year','')
    password=request.POST.get('password','')

    #every data inputed.
    error="invalid try again"
    #verifications.
    users=User.objects.all().filter(email=email)
    for i in users:
        error="email/ user already registered "
        return render(request,'signup.html',{'error' : error})

    users=User.objects.all().filter(mobile=mobile)
    for i in users:
        error="mobile/ user already registered "
        return render(request,'signup.html',{'error' : error})

    if(password=='' or password.__len__()>50 or password.__len__()<8 or password =='password' or password=='12345678'):
        error="invalid password"
        return render(request,'signup.html',{'error' : error})

    users=User.objects.all().filter(username=username)
    for i in users:
        error="username/ user already registered "
        return render(request,'signup.html',{'error' : error})

    p=User(name=name,username=username,email=email,mobile=mobile,clas=clas,year=year,password=password)
    p.save()
    return render(request,'login.html',)

def loginprocess(request):
    email=request.POST.get('email','')
    password=request.POST.get('password','')

    #input recived
    users=User.objects.all().filter(email=email)
    k=0
    for i in users:
        k=1
        if(i.password!=password):
            error="incorrect credentials"

            return render(request,'login.html',{'error' : error})
    if(k==0):
        error="incorrect credentials"
        return render(request,'login.html',{'error' : error})


    request.session['logid'] = i.uid
    return redirect('/blog/me')
def profile(request):
	try:
		id = request.session['logid']
	except Exception:
		return render(request,'login.html',{'error' : 'Please Login to Continue'  })
	usrs=User.objects.all().filter(uid=id)
	for u in usrs:
		a=0
	posts=Post.objects.all().filter(uid=u)
	return render(request,'profile.html',{'u':u,'posts':posts})

def profileview(request,pk):
	users=User.objects.all().filter(uid=pk)
	for u in users:
		a=0
	posts=Post.objects.all().filter(uid=u)
	return render(request,'profileview.html',{'u':u,'posts':posts})
def profileedit(request):
	try:
		id = request.session['logid']
	except Exception:
		return render(request,'login.html',{'error' : 'Please Login to Continue'  })
	usrs=User.objects.all().filter(uid=id)
	for u in usrs:
		a=0
	return redirect('/user/profile/edit/verified/'+str(u.uid))

class profEdit(UpdateView):
	model=User
	fields=['pic','cover','name','username','about','mobile','linkdin','github','college','clas','year']
	success_url='/user/profile'
