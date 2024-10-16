from django.urls import include, path
from tech import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("blogs", views.blogs, name="blogs"),
    path("services", views.service, name="services"),
    path("projets", views.projets, name="projets"),
     path("equipe", views.equipe, name="equipe"),
    path("pricing", views.pricing, name="pricing"),
    path("contact", views.contact, name="contact"),
    path("blogdetail/<str:title>", views.blogdetail, name="blogdetail"),
    

    path("register", views.register, name="register"),


]
