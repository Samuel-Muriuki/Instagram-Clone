from dataclasses import fields
import email
from django import forms
# Pre-built register form that connects to the pre-built model User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Like

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


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'profile_info']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'profile', ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['username', 'post']


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        exclude = ['username', 'post', 'control']
