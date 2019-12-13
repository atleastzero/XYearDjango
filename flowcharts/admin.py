from django.contrib import admin

from .models import Flowchart, Term, Course

class CourseInline(admin.StackedInline):
    model = Course
    extra = 0

class TermInline(admin.StackedInline):
    model = Term
    extra = 0

class FlowchartAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created', 'last_updated')
    inlines = [TermInline]

class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'flowchart')
    inlines = [CourseInline]

admin.site.register(Flowchart, FlowchartAdmin)
admin.site.register(Term, TermAdmin)