from django.contrib.auth.models import User as AuthUser
from django.db import models

from localee.models import fk


# Mock User model that should function alongside Django's authentication
# Either add a ForeignKey to Django's Builtin User or
# subclass the User in django.contrib.auth
class User(models.Model):
    """
    A Localee user.
    Essentially, an extension of Django's built-in User.
    """

    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
