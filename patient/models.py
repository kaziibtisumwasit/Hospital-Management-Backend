from django.db import models
from django.contrib.auth.models import User 
# Create your models here.



class Patient(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='patient/images/' , null=True , blank=True) ## ImageField is used to store image files. The upload_to argument is used to specify the directory where the image files will be stored. The null=True argument is used to specify that the field can be left blank in the database. The blank=True argument is used to specify that the field can be left blank in the form.
    mobile_no = models.CharField(max_length=12) 
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
