from django import forms
from django.contrib.auth.models import User

from .models import Link, Bookmark,UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class BookmarkSaveForm(forms.Form):
    url = forms.URLField(
        label='URL',
        widget=forms.TextInput(attrs={'size': 64})
    )

    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'size': 64})
    )

    tags = forms.CharField(
        label='Tags',
        required=False,
        widget=forms.TextInput(attrs={'size': 64})
    )

    share = forms.BooleanField(
        label='Share on the main page',
        required=False
    )

class SearchForm(forms.Form):
    query = forms.CharField(
        label='Enter a keyword to search for',
        widget=forms.TextInput(attrs={'size': 32})
    )

class FriendInviteForm(forms.Form):
    name = forms.CharField(label='Friend\'s Name')
    email = forms.EmailField(label='Friend\'s Email')

