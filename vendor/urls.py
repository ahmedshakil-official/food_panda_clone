from django.urls import path
from vendor import views
from core import views as core_views

urlpatterns = [
    path("", core_views.vendor_dashboard, name="vendor"),
    path("profile/", views.vendor_profile, name="vendor_profile"),
]
