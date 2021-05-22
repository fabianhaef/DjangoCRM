from django import forms
from .models import Lead


class LeadModelForm(forms.ModelForm):
    class Meta:
        # Model that the form is about
        model = Lead

        # add all the fields that you want to display in the form
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent'
        )


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)
