from django.db import models
from django.utils import timezone

class Email(models.Model):
    name = models.TextField()
    email = models.TextField()
