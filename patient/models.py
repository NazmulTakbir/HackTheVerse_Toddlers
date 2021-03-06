from django.db import models
from healthcare_workers.models import *

# Create your models here.
class Patient(models.Model):

    bed = models.OneToOneField(Bed, on_delete=models.DO_NOTHING)

    age = models.IntegerField()
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    patientID = models.IntegerField(unique=True)
    admissionDate = models.DateField(null=False)

    def __str__(self):
        return self.name


class PreviousPatient(models.Model):

    bed = models.ForeignKey(Bed, on_delete=models.DO_NOTHING)

    age = models.IntegerField()
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    admissionDate = models.DateField(null=False)
    releaseData = models.DateField(null=False)
    patientID = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
