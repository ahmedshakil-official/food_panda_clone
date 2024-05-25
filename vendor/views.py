from django.shortcuts import render
from vendor.models import Vendor


def vendor_profile(request):
    return render(request, "vendor/profile.html")
