from django.urls import path, include
from .views import home, dashboard

urlpatterns = [
    path("", home, name="home"),
    path("customer/dashboard", dashboard, name="customer-dashboard"),
    path("vendor/dashboard", dashboard, name="vendor-dashboard"),
]