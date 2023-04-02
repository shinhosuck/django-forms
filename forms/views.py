from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, UserRegisterForm
from django.shortcuts import render, redirect




def home_view(request):
    return render(request, "forms/home.html", context=None)


def register_view_backup(request):
    form = RegisterForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password1 = form.cleaned_data.get("password")
        password2 = form.cleaned_data.get("confirm_password")
    return render(request, "forms/register.html", context)

def register_view(request):
    form = UserCreationForm(request.POST or None)
    # form = UserRegisterForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        form.save()
        # username = form.cleaned_data.get("username")
        # password1 = form.cleaned_data.get("password1")
        # password2 = form.cleaned_data.get("password2")
        # print(username, password1, password2)
    return render(request, "forms/register.html", context)


def login_view(request):
    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("forms:home")
        return render(request, "forms/login.html", context={"form": form})
    context = {"form": form}
    return render(request, "forms/login.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("forms:login")
    return render(request, "forms/logout.html", context=None)