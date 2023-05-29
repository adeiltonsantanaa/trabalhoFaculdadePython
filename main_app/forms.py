from django import forms
from .models import EnderecoWeb

class URLForm(forms.ModelForm):
    class Meta:
        model = EnderecoWeb
        fields = ['url']
