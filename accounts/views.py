from django.contrib.auth.decorators import login_required

from django.contrib import messages, auth

from accounts.models import User, UserProfile
from vendor.forms import VendorForm

from accounts.utils import detect_user
from django.shortcuts import render, redirect
from accounts.forms import UserForm


# Create your views here.

def UserRegistration(request):
    if request.user and request.user.is_authenticated:
        messages.warning(request, "You are already logged in!")
        return redirect("my-account")

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect("registerUser")
        else:
            print(form.errors)
    else:
        form = UserForm()

    context = {'form': form}
    return render(request, "accounts/register-user.html", context=context)


def VendorRegistration(request):
    if request.user and request.user.is_authenticated:
        messages.warning(request, "You are already logged in!")
        return redirect("my-account")
    if request.method == "POST":
        user_form = UserForm(request.POST)
        vendor_form = VendorForm(request.POST, request.FILES)
        if user_form.is_valid() and vendor_form.is_valid():
            password = user_form.cleaned_data["password"]
            user = user_form.save(commit=False)
            user.set_password(password)
            user.role = User.VENDOR
            user.save()
            vendor = vendor_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request, "Your account has been created successfully! Please wait for the approval to "
                                      "complete!.")
            return redirect("registerVendor")
        else:
            print(user_form.errors)
            print(vendor_form.errors)
    else:
        form = UserForm()
    user_form = UserForm()
    vendor_form = VendorForm()
    context = {"user_form": user_form, "vendor_form": vendor_form}
    return render(request, "accounts/register-vendor.html", context=context)


@login_required(login_url="login")
def my_account(request):
    user = request.user
    url = detect_user(user)
    return redirect(url)


def login(request):
    if request.user and request.user.is_authenticated:
        messages.warning(request, "You are already logged in!")
        return redirect("home")
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("my-account")
        else:
            messages.error(request, "Email or Password is incorrect")
            return redirect("login")
    return render(request, "accounts/login.html")


@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    messages.info(request, "You have been logged out!")
    return redirect("login")
