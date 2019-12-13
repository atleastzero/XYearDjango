from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from flowcharts.models import Flowchart
from api.serializers import FlowchartSerializer

class FlowchartList(ListCreateAPIView):
    queryset = Flowchart.objects.all()
    serializer_class = FlowchartSerializer

class FlowchartDetail(RetrieveDestroyAPIView):
    queryset = Flowchart.objects.all()
    serializer_class = FlowchartSerializer