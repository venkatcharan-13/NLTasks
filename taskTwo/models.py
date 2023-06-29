from django.db import models
from django.contrib.auth.models import User

# Create your models here.

appCategory_choice=[
    ('Social_Media', 'Social Media'),
    ('Educational_app', 'Educational App'),
    ('Games_App', 'Games App'),
    ('Lifestyle_App', 'Lifestyle App'),
]

appSubCategory_choice=[
    ('Facebook', ' Facebook App'),
    ('Instagram', 'Instagram App'),
    ('SnapChat', 'Snapchat App'),
    ('Linkedin', 'Linkedin App'),
    ('Indeed', ' Indeed App'),
    ('Naukri', 'Naukri App'),
    ('Game of Thornes', 'GOT App'),
    ('The_hindu', 'Hindu App'),
]


class adminAddApp(models.Model):
    def __str__(self):
        return self.appName
    userId=models.ForeignKey(User, on_delete=models.CASCADE)
    appName = models.CharField(max_length=30)
    appLink=models.CharField(max_length=30)
    appCategory=models.CharField(max_length=50, choices=appCategory_choice, default='Social Media')
    appSubCategory=models.CharField(max_length=50, choices=appSubCategory_choice, default='Social Media')
    adminAppPoints=models.IntegerField()
    adminAppImage=models.FileField(upload_to='images/',max_length=500,null=True,blank=True,default=None)


class userAppTask(models.Model):
    def __str__(self):
        return self.userAppName
    # appId=models.AutoField(primary_key=True)
    # userId=models.ForeignKey(User, on_delete=models.CASCADE)
    # adminappId=models.ForeignKey(adminAddApp, on_delete=models.CASCADE)
    adminappId=models.IntegerField()
    userappid=models.IntegerField()
    userAppName = models.CharField(max_length=30)
    userAppPoints=models.IntegerField()
    userAppImage=models.ImageField(upload_to='uploadss/',max_length=200,null=True,blank=True)


