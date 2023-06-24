from django.shortcuts import render


# Create your views here.


def create_profile(request):
    return render(request, "accounts/create-profile.html")


def profile_details(request):
    return render(request, "accounts/details-profile.html")


def edit_profile(request):
    return render(request, "accounts/edit-profile.html")


def delete_profile(request):
    return render(request, "accounts/delete-profile.html")
