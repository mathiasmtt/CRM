from django import forms
from django.contrib.auth.models import User, Group

class UserGroupForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = User
        fields = ['groups']
