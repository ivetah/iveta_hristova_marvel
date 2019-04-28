from django.db import models

# Create your models here.

class Character(models.Model):
    def get_upload_to(self, filename):
        return 'character_images/%s' % ( filename)
    hero = models.CharField(max_length=128, null=True)
    first_name = models.CharField(max_length=128,null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=1,null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    gender = models.CharField(max_length=10)
    biography =  models.TextField(null=True, blank=True)
    eyes = models.CharField(max_length=128,null=True, blank=True)
    hair =  models.CharField(max_length=128,null=True, blank=True)
    profile_picture =  models.ImageField(upload_to=get_upload_to, null=True, blank=True)

    def __str__(self):
        return self.hero 

class Group(models.Model):
    def get_upload_to(self, filename):
        return 'group_images/%s' % ( filename)
    name  = models.CharField(max_length=128)
    profile_picture =  models.ImageField(upload_to=get_upload_to, null=True, blank=True)
    history =  models.TextField(null=True, blank=True)
    members =  models.ManyToManyField(Character, blank=True)
    def __str__(self):
        return self.name 


    
    

