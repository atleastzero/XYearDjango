from django.urls import path

from . import views

urlpatterns = [
    path('', views.FlowchartListView.as_view(), name='flowchart-list'),
    path('create/', views.FlowchartCreateView.as_view(), name='flowchart-new'),
    path('<str:slug>/', views.FlowchartDetailView.as_view(), name='flowchart-detail'),
]