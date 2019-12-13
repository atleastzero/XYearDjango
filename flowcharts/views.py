from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from flowcharts.models import Flowchart
from flowcharts.forms import FlowchartCreateForm

class FlowchartListView(ListView):
    model = Flowchart

    def get(self, request):
        flowcharts = self.get_queryset().all().order_by("-last_updated")
        return render(request, 'flowcharts/flowchart_list.html', {
            'flowcharts': flowcharts
        })

class FlowchartCreateView(CreateView):
    model = Flowchart

    def get(self, request, *args, **kwargs):
        return render(request, 'flowcharts/create.html', {
            'form': FlowchartCreateForm()
        })

    def post(self, request, *args, **kwargs):
        form = FlowchartCreateForm(request.POST)
        flowcharts = self.get_queryset().all()
        if form.is_valid():
            flowchart = form.save()
            flowchart.save()
            return render(request, 'flowcharts/flowchart_detail.html', {
                'flowchart': flowchart
            })
        else:
            return render(request, 'flowcharts/create.html', {
                'form': FlowchartCreateForm(),
                'failure': True
            })