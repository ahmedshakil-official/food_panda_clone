from django.urls import path
from accounts import views

urlpatterns = [
    path("register/user", views.UserRegistration, name="registerUser"),
    path("register/vendor", views.VendorRegistration, name="registerVendor"),
    path("me", views.my_account, name="my-account"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("register/user", views.UserRegistration, name="registerUser")
]