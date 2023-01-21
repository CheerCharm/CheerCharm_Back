from django.db import models

from accounts.models import TimestampZone
from charms.models import Charm


class Cheer(TimestampZone):
    charm = models.ForeignKey(
        Charm, on_delete=models.CASCADE, related_name='cheer')
    nickname = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f'{self.charm.title}({self.id})'
