from django.contrib.auth.decorators import login_required

from django.contrib import messages, auth
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode

from accounts.models import User, UserProfile
from vendor.forms import VendorForm

from accounts.utils import (
    detect_user,
    send_verification_email,
    send_password_reset_email,
)
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
            user.role = User.CUSTOMER
            user.save()
            # Send activation email
            send_verification_email(request, user)
            messages.success(request, "Your account has been created successfully!")
            return redirect("registerUser")
        else:
            print(form.errors)
    else:
        form = UserForm()

    context = {"form": form}
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
            # Send activation email
            send_verification_email(request, user)
            messages.success(
                request,
                "Your account has been created successfully! Please wait for the approval to "
                "complete!.",
            )
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


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        messages.error(request, "User not found")

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Congratulations! Your account has been activated!")
        return redirect("my-account")
    else:
        messages.error(request, "Your token is invalid or expired")
        return redirect("my-account")


def forgot_password(request):
    if request.method == "POST":
        email = request.POST["email"]

        if User.objects.get(email=email):
            user = User.objects.get(email__exact=email)

            send_password_reset_email(request, user)
            messages.success(
                request, "Your password rest link has been sent successfully!"
            )
            return redirect("login")
        else:
            messages.error(request, "Account doesn't exist, please try again!")
            return redirect("forgot_password")

    return render(request, "accounts/forgot_password.html")


def reset_password_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        messages.error(request, "User not found")

    if user is not None and default_token_generator.check_token(user, token):
        request.session["uid"] = uid
        messages.info(request, "Please reset your password to your new password!")
        return redirect("reset_password")
    else:
        messages.error(request, "Your token is invalid or expired")
        return redirect("my-account")


def reset_password(request):
    if request.method == "POST":
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            pk = request.session.get("uid")
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.save()
            messages.success(request, "Your password has been reset successfully!")
            return redirect("login")
        else:
            messages.error(request, "Passwords don't match")
            return redirect("reset_password")
    return render(request, "accounts/reset_password.html")
