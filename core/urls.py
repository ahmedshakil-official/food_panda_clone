from django.urls import path, include
from .views import home, vendor_dashboard, customer_dashboard

urlpatterns = [
    path("", home, name="home"),
    path("customer/dashboard", customer_dashboard, name="customer-dashboard"),
]
