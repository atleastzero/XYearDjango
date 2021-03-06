from django import forms

from .models import Flowchart, Term, Course

class DateInput(forms.DateInput):
    input_type = 'date'

class FlowchartCreateForm(forms.ModelForm):
    class Meta:
        model = Flowchart
        fields = "__all__"

class TermCreateForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = '__all__'
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'