from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from django.contrib.auth.forms import UserCreationForm

from tracker.models import Vaccination, Complication, Parent, Vaccine


class VaccinationCreateForm(forms.ModelForm):
    vaccine = forms.ModelChoiceField(queryset=Vaccine.objects.all())

    class Meta:
        model = Vaccination
        fields = ['vaccine']


class ComplicationCreateForm(forms.ModelForm):
    class Meta:
        model = Complication
        fields = ["description"]


class ParentCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Parent
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
        )
