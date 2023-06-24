from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.accounts.models import Profile
from fruitipedia_app.fruits.validators import only_letters_validator


# Create your models here.


class Fruit(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        validators=[
            MinLengthValidator(2),
            only_letters_validator
        ]
    )

    image_url = models.URLField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    nutrition = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
