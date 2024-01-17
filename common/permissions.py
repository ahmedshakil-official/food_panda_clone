from django.core.exceptions import PermissionDenied


def isVendor(user):
    if user.is_authenticated and user.role == 1:
        return True
    else:
        raise PermissionDenied


def isCustomer(user):
    if user.is_authenticated and user.role == 2:
        return True
    else:
        raise PermissionDenied
