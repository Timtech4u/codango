from django.db import models
# Create your models here.
"""
Models for contact us
"""
class ContactUsModel(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    subject = models.CharField(max_length=100, null=False)
    message = models.TextField(null=False)
    date_sent = models.DateTimeField(auto_now_add=True)

def  __str__(self):
    return self.message
