from django import forms
from . import models

class CreateItem(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ['name', 'description']