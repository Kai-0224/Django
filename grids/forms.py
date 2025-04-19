from django import forms
from .models import Grid

class GridForm(forms.ModelForm):
    class Meta:
        model = Grid
        fields = ['x', 'y', 'width', 'height']

