from django.core.exceptions import ValidationError


def first_char_validation(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")
