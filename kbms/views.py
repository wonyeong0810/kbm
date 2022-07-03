from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request, "kbms/info.html")

def books(request):
    return render(request, "kbms/books.html")

def book1(request):
    return render(request, "kbms/book1.html")

def book2(request):
    return render(request, "kbms/book2.html")

def book3(request):
    return render(request, "kbms/book3.html")