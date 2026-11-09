from django.contrib import admin
from . import models
# Register your models here.


class SpecializationModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name' , ),}


class DesignationModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name' , ),}
    
    
    
admin.site.register(models.Specialization,SpecializationModelAdmin) ## registering the model in the admin panel. The first argument is the model name and the second argument is the ModelAdmin class. By default, Django will use the default ModelAdmin class, but you can override it by creating a custom ModelAdmin class and passing it as the second argument. In this case, we are using the ContactModelAdmin class to customize the admin panel for the ContactUs model.
admin.site.register(models.Designation,DesignationModelAdmin) ## registering the model in the admin panel. The first argument is the model name and the second argument is the ModelAdmin class. By default, Django will use the default ModelAdmin class, but you can override it by creating a custom ModelAdmin class and passing
admin.site.register(models.AvailableTime) 
admin.site.register(models.Doctor) ## registering the model in the admin panel. The first argument is the model name and the second argument is the ModelAdmin class. By default, Django will use the default ModelAdmin class, but you can override it by creating a custom ModelAdmin class and passing it as the second argument. In this case, we are using the ContactModelAdmin class to customize the admin panel for the ContactUs model. 

admin.site.register(models.Review)
