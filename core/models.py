from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    subject = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    message = models.TextField()

    def __str__(self):
        return self.subject