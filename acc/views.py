from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password
# Create your views here.

def index(request):
    return render(request,"acc/index.html")

def login_user(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(request, u)
            return redirect("acc:index")
        else:
            pass
    return render(request, "acc/login.html")

def logout_user(request):
    logout(request)
    return redirect("acc:index")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("con")
        upic = request.FILES.get("pic")
        try:
            User.objects.create_user(username=un, password=up, content=uc, pic=upic)
            return redirect("acc:login")
        except:
            pass
    return render(request, "acc/signup.html")

def profile(request):
    return render(request, "acc/profile.html")

def reprofile(request):
    if request.method == "POST":
        u = request.user
        um = request.POST.get("umail")
        uc = request.POST.get("ucon")
        up = request.FILES.get("upic")
        u.email , u.content = um , uc
        if up:
            u.pic.delete()
            u.pic = up
        u.save()
        return redirect("acc:profile")
    return render(request, "acc/reprofile.html")

def repass(request):
    if request.method == "POST":
        u = request.user
        cp = request.POST.get("fpass")
        if check_password(cp, u.password):
            np = request.POST.get("lpass")
            u.set_password(np)
            u.save()
            return redirect("acc:login")
        else:
            pass
    return redirect("acc:profile")

def delete(request):
    u = request.user
    p = request.POST.get("pass")
    if check_password(p, u.password):
        request.user.delete()
        return redirect("acc:login")
    else:
        return redirect("acc:profile")
