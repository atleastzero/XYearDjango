from django.db import models

class Course(models.Model):
    code_subject = models.CharField(max_length=10)
    code_number = models.IntegerField(default=100)
    name = models.CharField(max_length=100)
    credit_hours = models.IntegerField()