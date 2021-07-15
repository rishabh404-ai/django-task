from django.contrib import admin
from myapp.models import *
# Register your models here.

class Taskadmin(admin.ModelAdmin):
    list_display =('id','title','user')

class TileAdmin(admin.ModelAdmin):
    list_display = ('id','launch_date')
    
admin.site.register(Task,Taskadmin)    
admin.site.register(Tile,TileAdmin)            
        
    