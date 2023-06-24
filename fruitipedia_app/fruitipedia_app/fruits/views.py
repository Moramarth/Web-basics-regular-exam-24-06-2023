from django.shortcuts import render


# Create your views here.

def create_fruit(request):
    return render(request, "fruits/create-fruit.html")


def fruit_details(request, pk):
    return render(request, "fruits/details-fruit.html")


def edit_fruit(request, pk):
    return render(request, "fruits/edit-fruit.html")


def delete_fruit(request, pk):
    return render(request, "fruits/delete-fruit.html")
