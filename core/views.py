from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render

from common.permissions import isVendor, isCustomer


# Create your views here.

def home(request):
    return render(request, "core/home.html")


@login_required(login_url="login")
@user_passes_test(isCustomer)
def customer_dashboard(request):
    return render(request, "core/customer_dashboard.html")


@login_required(login_url="login")
@user_passes_test(isVendor)
def vendor_dashboard(request):
    return render(request, "core/vendor_dashboard.html")
