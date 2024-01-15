from django.shortcuts import redirect


def detect_user(user):
    if user.role == 1:
        return "vendor-dashboard"
    elif user.role == 2:
        return "customer-dashboard"
    elif user.role is None and user.is_superuser:
        return "/admin"
