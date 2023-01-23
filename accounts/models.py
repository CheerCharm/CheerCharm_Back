from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class TimestampZone(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of username
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email=self.normalize_email(email), password=password, **extra_fields)


class User(AbstractUser, TimestampZone):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100)
    url_value = models.CharField(
        max_length=200, unique=True)  # max_length < 256

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'nickname']
    objects = CustomUserManager()

    def __str__(self):
        return self.username
