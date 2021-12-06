from django.db import models
from django.utils import timezone

# Create your models here.
class Subscripers(models.Model):
    email = models.EmailField(blank=True, null=True)
    subscription_date = models.DateTimeField(default=timezone.now)



class MailMessages(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
