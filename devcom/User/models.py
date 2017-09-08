from django.db import models

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.IntegerField()
    linkdin = models.CharField(max_length=50,null=True)
    github = models.CharField(max_length=50,null=True)
    college = models.CharField(max_length=40, default='College of Engineering Chengannur')
    clas = models.CharField(max_length=20)
    year = models.IntegerField()
    isteam=models.IntegerField(default=1)
    password=models.CharField(max_length=100)
    dp=models.CharField(max_length=200,null=True,default='/media/media/dp/pic_rOge5Ez.png')
    about=models.CharField(max_length=140,default='passionate developer. Skilled programmer . Devcom member')
    pic=models.ImageField(upload_to="media/dp",null=True)
    cover=models.ImageField(upload_to="media/cover",null=True)





    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.uid})
class Dp(models.Model):
    dpid=models.AutoField(primary_key=True)
    user=models.CharField(max_length=100)
    dp=models.ImageField(upload_to="media/dp")

    def __str__(self):
        return self.user
