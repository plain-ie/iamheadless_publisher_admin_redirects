from django import forms
from django.forms import formset_factory


class RedirectForm(forms.Form):
    source_url = forms.URLField(max_length=4096)
    destination_url = forms.URLField(max_length=4096)
