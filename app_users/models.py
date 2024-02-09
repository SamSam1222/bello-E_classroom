from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.user.username:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)




class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   
    image = models.ImageField(upload_to='user_images', blank=True, null=True)
 
    
    teachers = 'teachers'
    students = 'students'
    parents = 'parents'
    user_types = [
        (teachers, 'teachers'),
        (students, 'students'),
        (parents, 'parents'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types, default=students)
    
    def __str__(self):
        return self.user.username
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')
    