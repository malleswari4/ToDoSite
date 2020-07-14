from Tasks.models import *
from django import forms
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        # message=forms.CharField(widget=forms.Textarea(attr={"rows":3,"cols":3}))
        fields='__all__'