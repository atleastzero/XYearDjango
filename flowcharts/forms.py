from django import forms
from .models import Flowchart


class FlowchartCreateForm(forms.ModelForm):
    class Meta:
        model = Flowchart
        fields = "__all__"