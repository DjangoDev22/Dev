from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES= [
        ('MALE' , 'Male'),
        ('FEMALE' , 'Female'),
        ('OTHER' , 'Other'),
    ]
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to= 'user/', blank=True, null=True)
    bio= models.TextField(blank=True, null=True)
    location= models.CharField(max_length=120, blank=True, null=True)
    birthdate= models.DateField(blank=True, null=True)
    gender= models.CharField(max_length=120, choices=GENDER_CHOICES, blank=True, null=True)
    mobile= models.CharField(max_length=120, blank=True, null=True)
    age= models.IntegerField(blank=True, null=True)
    # job = models.CharField(max_length=120, blank=True, null=True)

    created_at= models.DateTimeField(default=timezone.now)
    updated_at= models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.user.username)

    class Meta:
        verbose_name= "Profile"
        verbose_name_plural= "Profiles"
