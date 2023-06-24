from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.accounts.validators import first_char_validation


# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        validators=[
            MinLengthValidator(2),
            first_char_validation,
        ]
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=35,
        validators=[
            MinLengthValidator(1),
            first_char_validation,
        ]
    )

    email = models.EmailField(blank=False, null=False, max_length=40)
    password = models.CharField(blank=False, null=False, max_length=20, validators=[MinLengthValidator(8)])
    image_url = models.URLField(blank=True, null=True)
    age = models.IntegerField(blank=True, default=18)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
