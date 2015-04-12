from django import forms

from .models import Registration, Car

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        exclude = []
