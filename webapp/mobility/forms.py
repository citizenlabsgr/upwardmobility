
from secrets import choice
from django import forms
from .choices_lists import METRIC_CHOICES, COUNTY_CHOICES

class MetricForm(forms.Form):
    metric = forms.ChoiceField(choices=METRIC_CHOICES)


class CountyForm(forms.Form):
    fips = forms.ChoiceField(choices=COUNTY_CHOICES, label="County")

class CountyCompareForm(forms.Form):
    fips1 = forms.ChoiceField(choices=COUNTY_CHOICES, label="First County")
    fips2 = forms.ChoiceField(choices=COUNTY_CHOICES, label="Second County")