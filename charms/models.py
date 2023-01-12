from django.db import models

from accounts.models import TimestampZone, User
from django.conf import settings 


class Charm(TimestampZone):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='charms')
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    total_cheer = models.PositiveIntegerField(null=True)
    cur_cheer = models.PositiveIntegerField(verbose_name='응원수', null=True, blank=True)
    is_created = models.BooleanField(default=False)
    class Image(models.IntegerChoices):
        monkey = 1
        mouse = 2
        rabbit = 3
        squirrel = 4
        goat = 5
        bird = 6
    image = models.IntegerField(choices=Image.choices, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
