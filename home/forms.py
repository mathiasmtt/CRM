from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False, max_length=30, label='First Name')
    last_name = forms.CharField(required=False, max_length=30, label='Last Name')
    email = forms.EmailField(required=True, label='Email')
    address = forms.CharField(required=False, max_length=255, label='Address')
    phone = forms.CharField(required=False, max_length=15, label='Phone')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'address', 'phone']
