from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import UserForm
from django.contrib import messages


# Create your views here.

def UserRegistration(request):
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
