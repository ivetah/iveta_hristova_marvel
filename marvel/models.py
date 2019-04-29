from django.db import models


class Group(models.Model):
    def get_upload_to(self, filename):
        return 'group_images/%s' % ( filename)

    name  = models.CharField(max_length=128)
    profile_picture =  models.ImageField(upload_to=get_upload_to, null=True, blank=True)
    history =  models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name 

class Character(models.Model):
    def get_upload_to(self, filename):
        return 'character_images/%s' % ( filename)
    hero = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=1,null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    gender = models.CharField(max_length=10)
    biography =  models.TextField(blank=True)
    eyes = models.CharField(max_length=128, blank=True)
    hair =  models.CharField(max_length=128, blank=True)
    profile_picture =  models.ImageField(upload_to=get_upload_to, null=True, blank=True)
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.hero 



    
    

