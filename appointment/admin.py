from django.contrib import admin
from . import models
# Register your models here.


class AppointmentAdmin(admin.ModelAdmin):## admin.ModelAdmin is use to customize the admin panel for the model. It allows you to specify various options and settings for the model, such as list display, search fields, filters, and more.
    list_display =['doctor_name' , 'patient_name' , 'appointment_type' , 'appointment_status' , 'symptoms' , 'time' , 'cancel']  ## If I don't use list_display its shows the __str__() method of the model in the list view of the admin panel. But if I use list_display it shows the fields specified in the list_display attribute in the list view of the admin panel.
    
    ## list_display is used for displaying the fields in the admin panel. It is a tuple of field names to be displayed in the list view of the model. By default, Django will display the __str__() method of the model, but you can override it using the list_display attribute in the ModelAdmin class. In this case, we are displaying the doctor, patient, appointment_date, appointment_time, and status fields in the list view of the Appointment model.
    
    
    def patient_name(self,obj):
        return obj.patient.user.first_name
    
    def doctor_name(self,obj):
        return obj.doctor.user.first_name
    
    
admin.site.register(models.Appointment,AppointmentAdmin)