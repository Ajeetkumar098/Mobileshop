from django import forms
from .models import phone,contact_us,profileimage,Apple

class phone_form(forms.ModelForm):
    class Meta:
        model = phone
        fields = '__all__'

class contact_us_form(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = '__all__'

class profileimageform(forms.ModelForm):
    class Meta:
        model = profileimage
        fields = '__all__'


class Apple_form(forms.ModelForm):
    class Meta:
        model = Apple
        fields = '__all__'
