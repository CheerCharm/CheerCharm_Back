from django.db import models

from accounts.models import TimestampZone, User
from django.conf import settings 


class Charm(TimestampZone):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='charms')
    title = models.CharField(max_length=200)
    content = models.TextField()
    total_cheer = models.PositiveIntegerField()
    cur_cheer = models.PositiveIntegerField()
    is_created = models.BooleanField(default=False)
    image = models.URLField()

    def __str__(self):
        return f'{self.title}'
