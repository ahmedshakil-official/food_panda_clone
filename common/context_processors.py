from django.conf import settings

from vendor.models import Vendor


def get_vendor(request):
    if request.user.is_authenticated:
        try:
            vendor = Vendor.objects.select_related("user_profile").get(
                user=request.user
            )
        except Vendor.DoesNotExist:
            vendor = None
    else:
        vendor = None
    return dict(vendor=vendor)


def get_google_api_key(request):
    return {"GOOGLE_API_KEY": settings.GOOGLE_API_KEY}
