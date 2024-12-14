from django.db import models
from django.contrib.auth.models import User 

class Post(models.Model):
     user =  models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
     title = models.CharField(max_length=255)
     created = models.DateTimeField(auto_now_add=True)
     body = models.TextField()
     
     def __str__(self):
         return self.title + ' | ' +  str(self.user)