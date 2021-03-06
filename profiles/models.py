from django.db import models
from core.models import TimestampedModel
from authentication.models import User

class Profile(TimestampedModel):
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )

    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

