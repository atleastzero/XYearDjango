from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from flowcharts.models import Flowchart, Term, Course
from api.serializers import FlowchartSerializer, TermSerializer, CourseSerializer

class FlowchartList(APIView):
    def get(self, request):
        flowcharts = Flowchart.objects.all()[:20]
        data = FlowchartSerializer(flowcharts, many=True).data
        return Response(data)

class FlowchartDetail(APIView):
    def get(self, request, pk):
        flowchart = get_object_or_404(Flowchart, pk=pk)
        data = FlowchartSerializer(flowchart).data
        return Response(data)