from django import forms
from .models import Devtool

class DevForm(forms.ModelForm):
  class Meta():
    model = Devtool
    fields = ('__all__')