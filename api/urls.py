from django.urls import path

from api.views import FlowchartList, FlowchartDetail

urlpatterns = [
    path('flowcharts/', FlowchartList.as_view(), name='flowchart_list'),
    path('flowcharts/<int:pk>', FlowchartDetail.as_view(), name='flowchart_detail')
]