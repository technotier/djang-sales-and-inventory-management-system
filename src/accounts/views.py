from django.shortcuts import render, redirect
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST.get("pass_word")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.warning(request, "Usrname or Password is Wrong. Try Again!")
            return redirect("user_login")
    return render(request, "user_login.html")

def user_logout(request):
        logout(request)
        return redirect("user_login")
    
def set_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            set_password_form = SetPasswordForm(user=request.user, data=request.POST)
            if set_password_form.is_valid():
                set_password_form.save()
                update_session_auth_hash(request, set_password_form.user)
                return redirect("user_login")
        else:
            set_password_form = SetPasswordForm(user=request.user)
    context = {
        "set_password_form": set_password_form
    }
    return render(request, "set_password.html", context)