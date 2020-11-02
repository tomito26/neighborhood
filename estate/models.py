from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)


class Business(models.Model):
    business_name =  models.CharField(max_length=100)
    business_owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    business_image = CloudinaryField(null=True)
    business_location = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)




    def __str__(self):
        return self.business_name


    def get_absolute_url(self):
        return reverse('business-detail',kwargs={'pk':self.pk})

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post = models.TextField(null=True)
    date_posted =models.DateTimeField(auto_now=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True,blank=True)
    
    
  
