from django.db import models

from accounts.models import TimestampZone, User

CHARM_CHOICE = (
    ('MONKEY', 'MONKEY'),
    ('MOUSE', 'MOUSE'),
    ('RABBIT', 'RABBIT'),
    ('SQUIRREL', 'SQUIRREL'),
    ('GOAT', 'GOAT'),
    ('BIRD', 'BIRD')
)


class Charm(TimestampZone):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='charm')
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    total_cheer = models.PositiveIntegerField(default=0)
    cur_cheer = models.PositiveIntegerField(default=0)
    is_created = models.BooleanField(default=False)
    image = models.CharField(choices=CHARM_CHOICE, max_length=50)

    def __str__(self):
        return f'{self.title}'
