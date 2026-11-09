from django.contrib import admin
from .models import Patient
# Register your models here.



class PatientModelAdmin(admin.ModelAdmin):
    list_display = ('image' , 'first_name' , 'last_name',  'mobile_no') ## list_display is used for displaying the fields in the admin panel. It is a tuple of field names to be displayed in the list view of the model. By default, Django will display the __str__() method of the model, but you can override it using the list_display attribute in the ModelAdmin class. In this case, we are displaying the name, phone, and problem fields in the list view of the ContactUs model.
    
    
    def first_name(self, obj):
        return obj.user.first_name
    def last_name(self, obj):
        return obj.user.last_name
    
admin.site.register(Patient , PatientModelAdmin) ## registering the model in the admin panel. The first argument is the model name and the second argument is the ModelAdmin class. By default, Django will use the default ModelAdmin class, but you can override it by creating a custom ModelAdmin class and passing it as the second argument. In this case, we are using the ContactModelAdmin class to customize the admin panel for the ContactUs model.