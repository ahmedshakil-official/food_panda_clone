from django.urls import path, include
from accounts import views

urlpatterns = [
    path("", views.my_account, name="my-account"),
    path("register/user/", views.UserRegistration, name="registerUser"),
    path("register/vendor/", views.VendorRegistration, name="registerVendor"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
    path("forgot_password", views.forgot_password, name="forgot_password"),
    path(
        "reset_password_validate/<uidb64>/<token>/",
        views.reset_password_validate,
        name="reset_password_validate",
    ),
    path("reset_password", views.reset_password, name="reset_password"),
    path("vendor/", include("vendor.urls")),
]
