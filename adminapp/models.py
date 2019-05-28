from django.db import models
from django.conf import settings


class StatusQuerySet(models.QuerySet):
    pass

class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model)


class About_Us(models.Model):
    user        =   models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, blank=True, null= True)    
    title       =   models.CharField(max_length=255, default= 'Enter title')
    content     =   models.TextField(default='Enter text')
    updated     =   models.DateTimeField(auto_now=True)
    timestamp   =   models.DateTimeField(auto_now_add=True)

    objects = StatusManager()
    
    def __str__(self):
        return str(self.content)[:50]


class Team_Members(models.Model):
    user        =   models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, blank=True, null= True)    
    name        =   models.CharField(max_length=255, default= 'Enter name')
    designation =   models.CharField(max_length=255, default='Enter designation')
    updated     =   models.DateTimeField(auto_now=True)
    timestamp   =   models.DateTimeField(auto_now_add=True)
    image       =   models.ImageField(upload_to='img/team',default='../media/img/default.jpg')
    url         =   models.CharField(max_length=255,default='./templates/base.html')


    objects = StatusManager()
    
    def __str__(self):
        return str(self.name)[:50]

#     class (models.Model):
#     user        =   models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, blank=True, null= True)    
#     title       =   models.CharField(max_length=255, default= 'Enter title')
#     content     =   models.TextField(default='Enter text')
#     updated     =   models.DateTimeField(auto_now=True)
#     timestamp   =   models.DateTimeField(auto_now_add=True)

#     objects = StatusManager()
    
#     def __str__(self):
#         return str(self.content)[:50]