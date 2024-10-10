# licenses/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class License(models.Model):
    key = models.CharField(max_length=255, unique=True)
    user_email = models.EmailField()
    issued_date = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField()
    is_revoked = models.BooleanField(default=False)

    def is_valid(self):
        return not self.is_revoked and timezone.now() < self.expiration_date

    def __str__(self):
        return self.key
