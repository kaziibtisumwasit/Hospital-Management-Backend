from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="service/images/") ## in service app create a images folder & in this folder save images
    # price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name