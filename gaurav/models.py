from django.db import models

# Create your models here.

class company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name= models.CharField( max_length=50)
    location=models.CharField(max_length=100)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=
                          (('it','it'),
                           ('non it','non it'),
                           ('mobiles phones','mobiles phones'),
                           ('marketing','marketing')
                           ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)