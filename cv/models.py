from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phno = models.CharField(max_length=15,unique=True)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    about = models.TextField(blank=True,null=True)
    linkdin = models.URLField(blank=True,null=True)
    github  = models.URLField(blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,default='Pruthvi')


    def __str__(self):
        return self.user.username

class Education(models.Model):
    sslc = models.CharField(max_length=100)
    puc = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    percentage = models.IntegerField(unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username


class Skill(models.Model):
    skill = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.skill

class Experience(models.Model):
    jobrole = models.CharField(max_length=50)
    companyname = models.CharField(max_length=70)
    projects = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.job_role
    