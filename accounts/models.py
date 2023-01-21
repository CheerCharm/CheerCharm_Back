from django.db import models
from django.contrib.auth.models import AbstractUser


class TimestampZone(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True

# email사용 안해서 뺐음
class User(TimestampZone):
    username=models.CharField(max_length=200, unique=True, default='')
    password = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100) #닉네임(유저 이름)
    url_value = models.CharField(max_length=2000, unique=True)

    def __str__(self):
        return self.username
