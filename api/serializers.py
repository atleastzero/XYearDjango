from rest_framework.serializers import ModelSerializer

from flowcharts.models import Flowchart, Term, Course

class FlowchartSerializer(ModelSerializer):
    class Meta:
        model = Flowchart
        fields = '__all__'

class TermSerializer(ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
