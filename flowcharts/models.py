from django.db import models
from datetime import datetime
from django.utils.text import slugify

class Flowchart(models.Model):
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    flowchart_slug = models.CharField(max_length=20, blank=True, editable=False)
    
    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.flowchart_slug = slugify(self.name, allow_unicode=True)

        # Call save on the superclass.
        return super(Flowchart, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Term(models.Model):
    name = models.CharField(max_length=30)
    start_date = models.DateField('start_date')
    end_date = models.DateField('end_date')
    flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)
    term_slug = models.CharField(max_length=20, blank=True, editable=False)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.term_slug = slugify(self.name, allow_unicode=True)

        # Call save on the superclass.
        return super(Term, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=30)
    subject = models.CharField(max_length=10)
    code = models.DecimalField(max_digits=10, decimal_places=4)
    prerequisites = models.ForeignKey('self', on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    course_slug = models.CharField(max_length=20, blank=True, editable=False)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.course_slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.subject, " ", self.code