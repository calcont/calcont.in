from django.db import models

# Create your models here.
class Headlines(models.Model):
    main_title=models.CharField(max_length=300)
    text=models.CharField(max_length=300)
    def __str__(self):
        return self.main_title
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=15)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name
class Donate(models.Model):
    Donater_id=models.AutoField(primary_key=True)
    Donater_name = models.CharField(max_length=122 ,default="")