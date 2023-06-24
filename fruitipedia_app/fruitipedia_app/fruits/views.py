from django.shortcuts import render, redirect, get_object_or_404

from fruitipedia_app.accounts.templatetags.custom_tags import profile_status
from fruitipedia_app.fruits.forms import FruitForm, FruitEditForm, FruitDeleteForm
from fruitipedia_app.fruits.models import Fruit


# Create your views here.

def create_fruit(request):
    form = FruitForm()

    if request.method == "POST":
        user = profile_status()
        data = request.POST.copy()
        data["created_by"] = user.pk
        form = FruitForm(data)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {"form": form}
    return render(request, "fruits/create-fruit.html", context)


def fruit_details(request, pk):
    fruit = get_object_or_404(Fruit, pk=pk)
    context = {"fruit": fruit}
    return render(request, "fruits/details-fruit.html", context)


def edit_fruit(request, pk):
    fruit = get_object_or_404(Fruit, pk=pk)
    form = FruitEditForm(instance=fruit)
    if request.method == "POST":
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {"form": form}
    return render(request, "fruits/edit-fruit.html", context)


def delete_fruit(request, pk):
    fruit = get_object_or_404(Fruit, pk=pk)
    form = FruitDeleteForm(instance=fruit)
    if request.method == "POST":
        fruit.delete()
        return redirect("dashboard")
    context = {"form": form}
    return render(request, "fruits/delete-fruit.html", context)
