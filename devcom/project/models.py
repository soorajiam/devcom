from django.db import models
from User.models import User

class Project(models.Model):
    projectid=models.AutoField(primary_key=True)
    projectname=models.CharField(max_length=100)
    tools=models.CharField(max_length=300)
    github=models.CharField(max_length=200)
    mentor=models.ForeignKey(User,on_delete=models.CASCADE)
    desc=models.CharField(max_length=1000)
    cover=models.ImageField(upload_to="media/blog/cover",null=True)

    def __str__(self):
        return self.projectname

class Team(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    approve=models.IntegerField(default=0)
    duty=models.CharField(max_length=200)

    def __str__(self):
        return ((self.project.projectname) +"/"+ (self.user.name))

class Stage(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    stageid=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    info=models.CharField(max_length=1000)
    date=models.DateField(null=True)

    def __str__(self):
        return ((self.project.projectname) +'/' + (self.user.name))



# Create your models here.
