from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.


class Visitor(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
    ]
    name=models.CharField(max_length=100)
    aadhar=models.IntegerField()
    email=models.CharField(max_length=20)
    inmate_name=models.CharField(max_length=50)
    relationship=models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    purpose=models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    admin_message = models.TextField(blank=True, null=True)  # Add this line



class Inmate(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    crime=models.CharField(max_length=100)
    sentence=models.CharField(max_length=100)
    entry_date = models.DateField()
    exit_date = models.DateField()
    img=models.ImageField(upload_to="pic")



class Report(models.Model):
    pro=models.ForeignKey(Inmate,related_name="report",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    reported_by=models.CharField(max_length=100,blank=True)
    desc=models.TextField()
    date=models.DateField()


class Work(models.Model):
    STATUS_CHOICES = [
        ('KITCHEN', 'kitchen'),
        ('CLEANING', 'cleaning'),
        ('GARDENING', 'gardening'),
        ('LIBRARY','library'),
        ('LAUNDRY','laundry'),
    ]   
    pro=models.ForeignKey(Inmate,related_name="work",on_delete=models.CASCADE)
    work = models.CharField(max_length=10, choices=STATUS_CHOICES, default='No Work Assigned')
    reported_by=models.CharField(max_length=100,blank=True)
    date=models.DateField()






