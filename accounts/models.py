from django.db import models


class TimestampZone(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class User(TimestampZone):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100)
    url_value = models.CharField(max_length=2000)
