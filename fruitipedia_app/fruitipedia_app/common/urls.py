from django.urls import path

from .views import index_page, display_dashboard

urlpatterns = [
    path("", index_page, name="home page"),
    path("dashboard/", display_dashboard, name="dashboard"),
]
