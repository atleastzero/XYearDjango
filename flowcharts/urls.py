from django.urls import path

from . import views

urlpatterns = [
    path('', views.FlowchartListView.as_view(), name='flowchart-list'),
]