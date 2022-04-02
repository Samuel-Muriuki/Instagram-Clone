from dataclasses import fields
import email
from django import forms
from django.contrib.auth.forms import UserCreationForm # Pre-built register form that connects to the pre-built model User
from django.contrib.auth.models import User

# Creating the forms here

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user