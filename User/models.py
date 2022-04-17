from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class User(AbstractUser):
    """customize django user model"""

    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Customer(User):
    class Meta:

        verbose_name = "Customer"
        verbose_name_plural = "Customer"

    def __str__(self):
        return self.username


class Bider(User):
    class Meta:
        verbose_name = "bider"
        verbose_name_plural = "bider"

    def __str__(self):
        return self.username
