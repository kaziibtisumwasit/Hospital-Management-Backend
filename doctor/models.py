from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
# Create your models here.



class Specialization(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100 , unique=True)
    
    def __str__(self):
        return self.name
    
    
class Designation(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100 , unique=True)
    
    def __str__(self):
        return self.name
    
    
class AvailableTime(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
    
class Doctor(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    image = models. ImageField(upload_to = 'doctor/images/' , null=True , blank=True)
    ## one doctor can have multipale designation & spilization. So we use ManyToManyField.
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Specialization)
    ## one doctor can have multiple available time , so we use one to many.
    available_time = models.ManyToManyField(AvailableTime )
    fees = models.IntegerField()
    meet_link = models.URLField(max_length=200 , null=True , blank=True)
    
    def __str__(self):
        return f"DR. {self.user.first_name} {self.user.last_name}"




    
STAR_CHOICES = (
    ('⭐' , '⭐'),
    ('⭐⭐' , '⭐⭐'),
    ('⭐⭐⭐' , '⭐⭐⭐'),
    ('⭐⭐⭐⭐' , '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐' , '⭐⭐⭐⭐⭐'),
)    
   
   
   

## one to many realtionship e many part e ForeignKey use hoi.
class Review(models.Model):
    # one doctor has multiple review . so one to many relationship e many part e ForeignKey use hoi.
    doctor = models.ForeignKey(Doctor , on_delete = models.CASCADE)
    reviewer = models.ForeignKey(Patient , on_delete = models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices = STAR_CHOICES , max_length=10)
    
    
    def __str__(self):
        return f"Patient : {self.reviewer.user.first_name + " " + self.reviewer.user.last_name } ; Doctor : {self.doctor.user.first_name + " " + self.doctor.user.last_name} "