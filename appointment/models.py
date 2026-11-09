from django.db import models
from doctor.models import Doctor ,AvailableTime
from patient.models import Patient 

# Create your models here.
## One doctor has multiple Appointments with different patients. So we use one to many relationship. In one to many relationship, the many part has a ForeignKey field that points to the one part. In this case, the Appointment model has a ForeignKey field that points to the Doctor model. This means that each Appointment is associated with one Doctor, but each Doctor can have multiple Appointments.
## One patient can take multiple appointments with different doctors. So we use one to many relationship.
## appointment part is many , so on  appointment model we use Foreignkey 

APPOINTMENT_STATUS = [
    ('Pending' , 'Pending'),
    ('Completed' , 'Completed'),
    ('Running' , 'Running'),
]

APPPOINTMENT_TYPE = [
    ('online' , 'online'),
    ('offline' , 'offline'),
]

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor , on_delete = models.CASCADE)
    patient = models.ForeignKey(Patient , on_delete = models.CASCADE)
    
    appointment_status = models.CharField(max_length=100, choices=APPOINTMENT_STATUS , default="Pending") ## default value is False. If the appointment is not confirmed, the status will be False. If the appointment is confirmed, the status will be True.
    appointment_type = models.CharField(max_length=100 , choices= APPPOINTMENT_TYPE) ## choices is used to limit the values that can be stored in the field. In this case, the types field can only have two values: 'online' or 'offline'.
    symptoms = models.TextField()
    time = models.OneToOneField(AvailableTime , on_delete = models.CASCADE)
    cancel = models.BooleanField(default=False) ## default value is False. If the appointment is not cancelled, the value will be False. If the appointment is cancelled, the value will be True. 
    
    
    def __str__(self):
        return f"Doctor : {self.doctor.user.first_name} , Patient : {self.patient.user.first_name}"
    