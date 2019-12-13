from django.db import models
from datetime import datetime

class Flowchart(models.Model):
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True)
    creates = models.DateTimeField(auto_now_add=True)

class Term(models.Model):
    name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)

class Course(models.Model):
    title = models.CharField(max_length=30)
    subject = models.CharField(max_length=10)
    code = models.DecimalField(max_digits=10, decimal_places=4)
    prerequisites = models.ForeignKey('self', on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)