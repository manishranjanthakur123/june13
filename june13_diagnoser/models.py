from django.db import models


# Create your models here.
def getuploadpath(instance, filename):
    return '/'.join(['medicalentity', str(instance.title), filename])


class MedicalEntity(models.Model):
    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(blank=True, null=True, upload_to=getuploadpath)
