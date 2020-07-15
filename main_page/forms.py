from django import forms

from .models import Main

class AddForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = '__all__'