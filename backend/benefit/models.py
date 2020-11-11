from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class AppConfig(models.Model):
    MEASUREMENT_SYSTEM_CHOISE = (
        ('METRIC', 'Metric'),
        ('IMPERIAL', 'Imperial')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    measurement_system = models.CharField(max_length=8, choices=MEASUREMENT_SYSTEM_CHOISE, default='METRIC')
 
    def __str__(self):
        return self.user.username


class Profile(models.Model):
    GENDER_CHOISE = (
        ('MALE', 'Male'),      # MALE - в базе данных , Male - то как отображается в админке.
        ('FEMALE', 'Female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    height = models.IntegerField(validators=[MinValueValidator(1)])
    weight = models.IntegerField(validators=[MinValueValidator(1)])
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOISE)

    def __str__(self):
        return self.user.username