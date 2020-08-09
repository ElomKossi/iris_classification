from django import forms
from .models import PredResults


class PredResultsForm(forms.ModelForm):
    class Meta:
        model = PredResults
        exclude = ('classification', )