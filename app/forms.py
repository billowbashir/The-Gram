from django import forms
fromm .models import Image

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['post_date']
        
