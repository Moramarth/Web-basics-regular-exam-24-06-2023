from django.shortcuts import render


# Create your views here.

def index_page(request):
    return render(request, "common/index.html")


def display_dashboard(request):
    return render(request, "common/dashboard.html")
