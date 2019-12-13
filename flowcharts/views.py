from django.shortcuts import render
from django.views.generic.list import ListView

from flowcharts.models import Flowchart

class FlowchartListView(ListView):
    model = Flowchart
    template_name='flowchart_list.html'

    def get(self, request):
        flowcharts = self.get_queryset().all().order_by("-last_updated")
        return render(request, self.template_name, {
            'flowcharts': flowcharts
        })