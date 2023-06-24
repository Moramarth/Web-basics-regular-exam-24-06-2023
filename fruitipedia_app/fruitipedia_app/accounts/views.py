from django.shortcuts import render, redirect

from fruitipedia_app.accounts.forms import ProfileForm, ProfileEditForm
from fruitipedia_app.accounts.templatetags.custom_tags import profile_status


# Create your views here.


def create_profile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("dashboard")
    context = {"form": form}
    return render(request, "accounts/create-profile.html", context)


def profile_details(request):
    return render(request, "accounts/details-profile.html")


def edit_profile(request):
    user = profile_status()
    form = ProfileEditForm(instance=user)
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile details")

    context = {"form": form}
    return render(request, "accounts/edit-profile.html", context)


def delete_profile(request):
    user = profile_status()
    if request.method == "POST":
        user.delete()
        return redirect("home page")
    return render(request, "accounts/delete-profile.html")
