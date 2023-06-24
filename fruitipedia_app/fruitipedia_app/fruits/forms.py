from django import forms

from fruitipedia_app.fruits.models import Fruit


class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Fruit Name"}),
            "image_url": forms.TextInput(attrs={"placeholder": "Fruit Image URL"}),
            "description": forms.Textarea(attrs={"placeholder": "Fruit Description"}),
            "nutrition": forms.Textarea(attrs={"placeholder": "Nutrition Info"}),
            "created_by": forms.HiddenInput(),
        }

        labels = {
            "name": "",
            "image_url": "",
            "description": "",
            "nutrition": "",
        }


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"

        labels = {
            "name": "Name:",
            "image_url": "Image URL:",
            "description": "Description:",
            "nutrition": "Nutrition:",
        }

        widgets = {
            "created_by": forms.HiddenInput(),
        }


class FruitDeleteForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ["created_by", "nutrition"]

        labels = {
            "name": "Name:",
            "image_url": "Image URL:",
            "description": "Description:",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["disabled"] = "disabled"


