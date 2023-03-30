from django import forms

from tracker.models import Vaccination, Complication


class VaccinationCreateForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = ["vaccine"]


class ComplicationCreateForm(forms.ModelForm):
    class Meta:
        model = Complication
        fields = ["description"]

