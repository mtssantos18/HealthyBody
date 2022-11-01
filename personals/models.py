from django.db import models

from email.policy import default
from django.db import models
import uuid


class Personal(models.Model):
    check_in = models.TimeField(auto_now=False, auto_now_add=False)
    check_out = models.TimeField(auto_now=False, auto_now_add=False)
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
