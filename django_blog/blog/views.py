from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from .forms import RegistrationForm, UserUpdateForm, ProfileForm

# --- Auth views using Django built-ins ---
class UserLoginView(LoginView):
    template_name = "blog/login.html"

class UserLogoutView(LogoutView):
    template_name = "blog/logout.html"


# --- Custom registration ---
def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in immediately after registration
            messages.success(request, "Welcome! Your account has been created.")
            return redirect("home")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = RegistrationForm()
    return render(request, "blog/register.html", {"form": form})


# --- Profile (view + edit) ---
@login_required
def profile_view(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    return render(request, "blog/profile.html", {"u_form": u_form, "p_form": p_form})


# --- (Optional) simple Home view so navbar links work ---
def home_view(request):
    return render(request, "blog/home.html")

