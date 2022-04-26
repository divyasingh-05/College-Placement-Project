from django import forms
from .models import Records


class Record_form(forms.ModelForm):
    class Meta:
        model=Records
        fields="__all__"
