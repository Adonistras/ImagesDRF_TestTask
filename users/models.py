from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CHOOSE_GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=10, choices=CHOOSE_GENDER, verbose_name='Gender', default='Male')

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-date_joined']