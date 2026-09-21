from django import forms
from .models import Contact


class Contact_Form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'your first name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'your last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your email',
            }),
            'subject':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'your subject',
            }),
        }