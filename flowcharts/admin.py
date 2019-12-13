from django.contrib import admin

from .models import Flowchart

class FlowchartAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created', 'last_updated')

admin.site.register(Flowchart, FlowchartAdmin)