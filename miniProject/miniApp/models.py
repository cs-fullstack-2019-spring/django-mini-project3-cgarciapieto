from django.db import models
from django.utils import timezone


class TeacherModel(models.Model):
    TeacherName = models.CharField(max_length=200)
    school =models.CharField(max_length=200)
    subject =models.CharField(max_length=200)
    hours =models.IntegerField(default=0)


    # i was gonna figure this after i got most the pages working, im still having trouble with date time and it interferes with the model being migrated

    # dateOfWork = models.DateField()
    # dateOfEntry = models.DateField


def __str__(self):
    return self.Teachername
