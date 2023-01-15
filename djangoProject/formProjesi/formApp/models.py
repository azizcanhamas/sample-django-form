from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

    jobs=[
        ('CE','Computer Engineering'),
        ('EEE','Electrical-Electronics Engineering'),
        ('CiE','Civil Engineering'),
        ('ME','Mechanical Engineering')

    ]
    job=models.CharField(max_length=3,choices=jobs,default=jobs[0][0])
