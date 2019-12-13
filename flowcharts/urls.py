from django.urls import path

from . import views

urlpatterns = [
    path('', views.FlowchartListView.as_view(), name='flowchart-list'),
    path('create/', views.FlowchartCreateView.as_view(), name='flowchart-new'),
    path('<str:flowchart_slug>/', views.FlowchartDetailView.as_view(), name='flowchart-detail'),
    path('<str:flowchart_slug>/create_term', views.TermCreateView.as_view(), name='term-new'),
    path('<str:flowchart_slug>/<str:term_slug>', views.TermDetailView.as_view(), name='term-detail'),
]