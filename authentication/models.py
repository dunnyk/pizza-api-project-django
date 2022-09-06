from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('email is required'))
        # normalizing email makes it to be in lower case like required.
        email = self.normalize_email(email)
        new_user = self.model(email=email, **extra_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser should have stuff as True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser should have is_subperuser as True'))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser should have is_active as True'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(_('Username'), max_length=25, unique=True)
    email = models.EmailField(_('Email'), max_length=80, unique=True)
    phone_number = PhoneNumberField(null=False, unique=True, blank=False)

    USERNAME_FIELD: 'email'  # this field helps when you want to log into the system
    REQUIRED_FIELDS = ['email', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
