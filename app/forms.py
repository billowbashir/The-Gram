from django import forms
from .models import Image,Profile

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['post_date','likes','comments','user']
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_pic','bio']
