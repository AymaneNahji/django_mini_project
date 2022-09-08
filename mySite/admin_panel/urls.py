from . import views
from django.urls import path

urlpatterns = [
    path("admin",views.login,name="login"),
    path("panel",views.panel,name="panel"),
    path("add",views.add_article,name="add"),
    path("up",views.updateArticle,name="upart"),
    path("del",views.deleteArticle,name="delart"),
    path("",views.home,name="home"),
    path("art",views.art,name="art")
]