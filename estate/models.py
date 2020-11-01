from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
class Business(models.Model):
    business_name =  models.CharField(max_length=100)
    business_owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    business_image = CloudinaryField(null=True)
    
  
    
    
    def __str__(self):
      return self.business_name
    
    
    def get_absolute_url(self):
      return reverse('business-detail',kwargs={'pk':self.pk})
    
    