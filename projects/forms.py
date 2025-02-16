from django import forms
from .models import Project
from django_select2.forms import Select2MultipleWidget

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date', 'stakeholders', 'status')
        widgets = {
            'stakeholders': Select2MultipleWidget(attrs={'class': 'form-control'}),
        }