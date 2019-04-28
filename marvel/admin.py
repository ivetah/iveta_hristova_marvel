from django.contrib import admin
from .models import *
# Register your models here.


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('hero','first_name' , 'last_name', )
admin.site.register(Character, CharacterAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name' ,)
admin.site.register(Group, GroupAdmin)