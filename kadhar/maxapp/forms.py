
from django import forms
from .models import *

class TableForm(forms.ModelForm):
    class Meta:
        model = table
        fields = '__all__'