from django.db import models
import uuid


class Customer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    