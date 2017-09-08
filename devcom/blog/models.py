from django.db import models
from User.models import User

class Topic(models.Model):
    topic=models.AutoField(primary_key=True)
    topicname=models.CharField(max_length=50)
    def __str__(self):
        return self.topicname

class Post(models.Model):
    postid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE,null=True)
    likes=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    cover=models.ImageField(upload_to="media/blog/cover",null=True)

    def __str__(self):
        return self.title

class Like(models.Model):
    likedby=models.ForeignKey(User,on_delete=models.CASCADE)
    forpost=models.ForeignKey(Post,on_delete=models.CASCADE)
    def __str__(self):
        return (self.likedby.name)

class Comment(models.Model):
    commentby=models.ForeignKey(User,on_delete=models.CASCADE)
    commentpost=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.CharField(max_length=500,null='false')
    order=models.AutoField(primary_key=True)

    def __str__(self):
        return self.commentby.name+','+self.commentpost.title




# Create your models here.
