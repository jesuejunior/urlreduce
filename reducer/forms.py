from django.forms import URLField, TextInput, ModelForm
from reducer.models import Link

__author__ = 'jesuejunior'

class ReduceURLForm(ModelForm):
    url = URLField(widget=TextInput(attrs={
        'placeholder': 'Digite a URL aqui.',
    }))

    class Meta:
        model = Link