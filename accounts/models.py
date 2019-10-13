# ACCOUNTS MODELS.PY FILE

from django.db import models
from django.contrib.auth import models
from django.utils import timezone

# from allauth.socialaccount.models import SocialToken, SocialAccount

# Create your models here.
class User(models.User, models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
