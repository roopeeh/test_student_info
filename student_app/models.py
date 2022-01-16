
from django.db import models
from django.db.models.deletion import CASCADE


class StudentInfo(models.Model):
    Roll_no = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30, null=True)
    Class = models.CharField(max_length=30, null=True)
    School = models.CharField(max_length=30, null=True)
    mobile = models.CharField(max_length=10, null=True)
    Address = models.CharField(max_length=50, null=True)


class StudentAcademics(models.Model):
    Student = models.OneToOneField(
        StudentInfo, on_delete=models.CASCADE, null=True)
    Maths = models.IntegerField(default=None, null=True)
    Physics = models.IntegerField(default=None, null=True)
    Chemistry = models.IntegerField(default=None, null=True)
    Biology = models.IntegerField(default=None, null=True)
    English = models.IntegerField(default=None, null=True)
