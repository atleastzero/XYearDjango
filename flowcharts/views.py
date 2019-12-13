from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from flowcharts.models import Flowchart
from flowcharts.forms import FlowchartCreateForm

class FlowchartListView(ListView):
    model = Flowchart

    def get(self, request):
        flowcharts = self.get_queryset().all().order_by("-last_updated")
        return render(request, 'flowcharts/flowchart_list.html', {
            'flowcharts': flowcharts
        })

class FlowchartDetailView(DetailView):
    model = Flowchart

    def get(self, request, slug):
        flowchart = get_object_or_404(Flowchart, slug__iexact=slug)
        return render(request, 'flowcharts/flowchart_detail.html', {
            'flowchart': flowchart
        })

class FlowchartCreateView(CreateView):
    model = Flowchart

    def get(self, request, *args, **kwargs):
        return render(request, 'flowcharts/create.html', {
            'form': FlowchartCreateForm()
        })

    def post(self, request, *args, **kwargs):
        form = FlowchartCreateForm(request.POST)
        if form.is_valid():
            flowchart = form.save()
            flowchart.save()
            return redirect("/", flowchart.slug)
        else:
            return render(request, 'flowcharts/create.html', {
                'form': FlowchartCreateForm(),
                'failure': True
            })