from django.forms import ModelForm, BooleanField
from .models import Post, Author
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


class NewsForm(ModelForm):
    check_box = BooleanField(label='Даю себе отчет')

    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'postCategory', 'postPhoto']


class UserForm(ModelForm):
    check_box = BooleanField(label='Даю себе отчет')

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email']