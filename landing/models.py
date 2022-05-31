from django.db import models

# Create your models here.
class GetMeNotified(models.Model):
    user_email = models.EmailField(null=True, blank=True)