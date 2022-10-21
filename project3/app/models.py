from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Patient(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255, null = True)
    last_name = models.CharField(max_length=255, null = True)
    email = models.CharField(max_length=255, null = True)
    phone = models.CharField(max_length=255, null = True)
    #profile_pic = models.ImageField(null=True, blank=True, default="profile2.png")
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.user}'



class Appointment(models.Model):

    Status = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled')
    )

    patient = models.ForeignKey(Patient, null=True, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 255, choices = Status, default = 'Pending')
    accepted_date = models.DateTimeField(null=True, blank = True)

    def __str__(self):
        return f'{self.patient }: {self.status}'