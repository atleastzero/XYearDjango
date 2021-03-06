from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from flowcharts.models import Flowchart, Term, Course
from flowcharts.forms import FlowchartCreateForm, TermCreateForm, CourseCreateForm

class FlowchartListView(ListView):
    model = Flowchart

    def get(self, request):
        flowcharts = self.get_queryset().all().order_by("-last_updated")
        return render(request, 'flowcharts/flowchart_list.html', {
            'flowcharts': flowcharts
        })

class FlowchartDetailView(DetailView):
    model = Flowchart

    def get(self, request, flowchart_slug):
        flowchart = get_object_or_404(Flowchart, flowchart_slug__iexact=flowchart_slug)
        return render(request, 'flowcharts/flowchart_detail.html', {
            'flowchart': flowchart
        })

class FlowchartCreateView(CreateView):
    model = Flowchart

    def get(self, request, *args, **kwargs):
        return render(request, 'flowcharts/flowchart_create.html', {
            'form': FlowchartCreateForm()
        })

    def post(self, request, *args, **kwargs):
        form = FlowchartCreateForm(request.POST)
        if form.is_valid():
            flowchart = form.save()
            flowchart.save()
            return redirect("/", flowchart.flowchart_slug)
        else:
            return render(request, 'flowcharts/flowchart_create.html', {
                'form': FlowchartCreateForm(),
                'failure': True
            })

class TermDetailView(DetailView):
    model = Term

    def get(self, request, flowchart_slug, term_slug):
        term = get_object_or_404(Term, term_slug__iexact=term_slug)
        return render(request, 'flowcharts/term_detail.html', {
            'term': term
        })

class TermCreateView(CreateView):
    model = Term

    def get(self, request, flowchart_slug, *args, **kwargs):
        return render(request, 'flowcharts/term_create.html', {
            'form': TermCreateForm()
        })

    def post(self, request, flowchart_slug, *args, **kwargs):
        form = TermCreateForm(request.POST)
        if form.is_valid():
            term = form.save()
            term.save()
            return redirect("/" + flowchart_slug + "/" + term.term_slug)
        else:
            return render(request, 'flowcharts/term_create.html', {
                'form': TermCreateForm(),
                'failure': True
            })

class CourseDetailView(DetailView):
    model = Course

    def get(self, request, flowchart_slug, term_slug, course_slug):
        course = get_object_or_404(Course, course_slug__iexact=course_slug)
        return render(request, 'flowcharts/course_detail.html', {
            'course': course
        })

class CourseCreateView(CreateView):
    model = Course

    def get(self, request, flowchart_slug, *args, **kwargs):
        return render(request, 'flowcharts/course_create.html', {
            'form': CourseCreateForm()
        })

    def post(self, request, flowchart_slug, term_slug, *args, **kwargs):
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            course = form.save()
            course.save()
            return redirect("/" + flowchart_slug + "/" + term_slug + "/" + course.course_slug)
        else:
            return render(request, 'flowcharts/course_create.html', {
                'form': CourseCreateForm(),
                'failure': True
            })