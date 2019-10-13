from __future__ import absolute_import,unicode_literals

from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect
from .models import Playlist

from braces.views import LoginRequiredMixin

######
# from accounts.models import User
# or
# Returns the User model that is active in this project
from django.contrib.auth import get_user_model
# call things off of the current user session
User = get_user_model()
######

# PlaylistListView
class HomePage(generic.ListView):
    template_name = 'playlists/home.html'
    model = Playlist
