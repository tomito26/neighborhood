from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)

    def save_neighborhood(self):
        self.save()

    @classmethod
    def delete_neighborhood(cls,id):
        cls.objects.filter(id).delete()
    @classmethod
    def update_neighborhood(cls,id,new_name):
        cls.objects.filter(id=id).update(hood_name = new_name)

    @classmethod
    def update_family_count(cls,id,new_occupant):
        cls.objects.filter(id=id).update(family_size =new_occupant)

    @classmethod
    def search_hood(cls, search_term):
        hood = cls.objects.filter(hood_name__icontains=search_term)
        return hood


class Business(models.Model):
    name =  models.CharField(max_length=100)
    business_owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    business_image = CloudinaryField(null=True)
    business_location = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)
    location = models.CharField(max_length=100,null=True,blank=True)

    def save_business(self):
        self.save()

    @classmethod
    def delete_business(cls, id):
        cls.objects.filter(id).delete()

    @classmethod
    def update_business(cls, id, new_name):
        cls.objects.filter(id=id).update(name=new_name)

    @classmethod
    def search_by_title(cls,search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('business-detail',kwargs={'pk':self.pk})

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post = models.TextField(null=True)
    date_posted =models.DateTimeField(auto_now=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True,blank=True)


    def get_absolute_url(self):
        return reverse('post')
