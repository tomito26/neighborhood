from django.db import models
from django.contrib.auth.models import User

class Business(models.Model):
    business_name =  models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    business_email = models.EmailField()
    
    
    def __str__(self):
      return self.business_name