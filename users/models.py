from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add a new field called `bio`.
    bio = models.CharField(max_length=100)

    # Customize the `username` field to be required.
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': 'A user with that username already exists.',
        },
    )

    # Customize the `is_active` field to be False by default.
    is_active = models.BooleanField(default=False)
