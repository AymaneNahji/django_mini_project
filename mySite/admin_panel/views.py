import json
import os
from string import whitespace
from uuid import uuid1
from django.shortcuts import redirect, render

from .models import User, Article
from django.http import HttpResponse

# Create your views here.

def isLogged(request):
    try:
        u = User.objects.get(
            user_name=request.session["un"], password=request.session["pass"])
        return True
    except:
        return False

def login(req):
    if (req.method == "POST"):
        user_name = req.POST.get("user_name")
        password = req.POST.get("password")
        try:
            u = User.objects.get(user_name=user_name, password=password)
            req.session["un"] = user_name
            req.session["pass"] = password
            return redirect("panel")
        except:
            print("la")
    return render(req, 'admin/login.html')


def panel(req):
    if isLogged(req):
        return render(req, 'admin/articles.html', {"arts": Article.objects.all()})
    else:
        return redirect("login")


def add_article(req):
    if isLogged(req):
        if (req.method == "POST"):
            pic = req.FILES.get("image")
            title = req.POST.get("title")
            content = req.POST.get("content")
            # str(uuid1())+"."+str(pic.content_type).split('/')[1]
            while True:
                s = "media/" + str(uuid1())+"."+str(pic.content_type).split('/')[1]
                if (os.path.exists(s)):
                    pass
                else:
                    print(s)
                    f = open(s, "wb")
                    f.write(pic.read())
                    f.close()
                    art = Article(title=title, content=content, image=str(s))
                    art.save()
                    break
            return redirect("panel")
        return render(req, 'admin/add_art.html')
    else:
        return redirect("login")

def updateArticle(req):
    if isLogged(req):
        if (req.method == "POST"):
            b = json.loads(req.body)

            try:
                try:
                    t = b['title']
                    art = Article.objects.get(pk=b['id'])
                    art.title = t
                    art.save()
                    print(t)
                    return HttpResponse("true")
                except:
                    c = b['content']
                    art = Article.objects.get(pk=b['id'])
                    art.content = c
                    art.save()
                    print(c)
                    return HttpResponse("true")
            except:
                print("nnn")
                return HttpResponse("false")
    else:
        return redirect("login")


def deleteArticle(req):
    if isLogged(req):
        art = Article.objects.get(pk=req.GET.get("id"))
        os.remove(art.image)
        art.delete()
        return redirect("panel")
    else:
        return redirect("login")

###########################
#client

def home(req):
    return render(req, 'client/home.html', {"arts": Article.objects.all()})

def art(req):
    try:
        a = Article.objects.get(pk=req.GET.get("id"))
        return render(req,"client/oneArticle.html",{"art":a})
    except:
        return redirect("home")