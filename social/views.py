# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import models, forms

# Create your views here.

# When someone's logged into a session, I can call this user object and call things off of that
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

# PlaylistListView
class HomePage(generic.ListView):
    template_name = 'playlists/home.html'
