from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    image_path = forms.CharField(label='Image Path', required=False)
    class Meta:
        model = Person
        fields = ['name', 'address', 'mobile_number', 'email', 'image_path']