from django import forms
from django.contrib.auth.models import User
from app_users.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'displayname': forms.TextInput(attrs={'placeholder':'Add display name', 'class':'form-control'}),
            'info':forms.Textarea(attrs={'rows':3, 'placeholder':'Add information', 'class':'form-control'})
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control me-2'})
    )

    class Meta:
        model = User
        fields = ['email']