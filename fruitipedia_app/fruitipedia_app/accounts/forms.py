from django import forms

from fruitipedia_app.accounts.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["age", "image_url"]

        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
        }

        labels = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "password": "",
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["password", "email"]

        labels = {
            "first_name": "First Name:",
            "last_name": "Last Name:",
            "image_url": "Image URL:",
            "age": "Age:",
        }
