from django import forms
from . import models


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = models.User
        exclude = ['picture', 'is_active', 'is_staff', 'date_joined']