from django.shortcuts import redirect, render

from acc.models import User

from .models import Board, Reply
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    page = request.GET.get("page", 1)
    kw = request.GET.get("kw","")
    cate = request.GET.get("cate","")
    if kw:
        if cate == "sub":
            b = Board.objects.filter(subject__startswith=kw)
        elif cate == "wri":
            try:
                u = User.objects.get(username=kw)
                b = Board.objects.filter(writer=u)
            except:
                b = Board.objects.none()
        elif cate == "con":
            b = Board.objects.filter(content__contains=kw)
        else:
            b = Board.objects.none()
    else:
        b = Board.objects.all()
    pag = Paginator(b, 5)
    obj = pag.get_page(page)
    
    

    context = {
        "bset" : obj,
        "cate" : cate,
        "kw" : kw
    }
    return render(request, "board/index.html", context)

def detail(request, bpk):
    b = Board.objects.get(id=bpk)
    r = b.reply_set.all() #댓글 다 나와
    context = {
        "b" : b,
        "rset" : r
    }
    return render(request, "board/detail.html", context)

def delete(request, bpk):
    b = Board.objects.get(id=bpk)
    if request.user == b.writer:
        b.delete()
    else:
        pass
    return redirect("board:index")

def create(request):
    if request.method == "POST":
        s = request.POST.get("sub")
        c = request.POST.get("con")
        Board(subject=s,writer=request.user,content=c).save()
        return redirect("board:index")

    return render(request, "board/create.html")

def update(request, bpk):
    b = Board.objects.get(id=bpk)

    if request.user != b.writer:
        pass
        return redirect("board:index")

    context = {
        "b" : b
    }
    if request.method == "POST":
        s = request.POST.get("sub")
        c = request.POST.get("con")
        b.subject, b.content = s, c
        b.save()
        return redirect("board:detail", bpk)
    return render(request, "board/update.html", context)

def write(request, bpk):
    b = Board.objects.get(id=bpk)
    c = request.POST.get("content")
    Reply(b=b,replyer=request.user,comment=c).save()
    return redirect("board:detail", bpk)

def dreply(request, bpk, rpk):
    r = Reply.objects.get(id=rpk)
    if request.user == r.replyer:
        r.delete()
    else:
        pass
    return redirect("board:detail", bpk)