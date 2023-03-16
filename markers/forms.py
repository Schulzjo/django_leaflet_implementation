from django import forms
from markers.models import Marker


class MarkerForm(forms.ModelForm):
    class Meta:
        model = Marker
        fields = ('name', 'latitude', 'longitude')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Name'}),
            'latitude': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': '13.123'}),
            'longitude': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': '2.123'}),
        }

