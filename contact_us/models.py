from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    problem = models.TextField()
    
    def __str__(self):
        return self.name
    
    
    class Meta: ## class Meta is used for modifying the default behavior of the model. It allows you to specify various options and settings for the model, such as database table name, ordering, verbose names, and more.
        verbose_name_plural = "Contact Us" ## using for changing the model name in admin panel. By default, Django will use the model's class name as the verbose name, but you can override it using the verbose_name attribute in the Meta class. In this case, we are setting the verbose name to "Contact Us" instead of the default "ContactUs".