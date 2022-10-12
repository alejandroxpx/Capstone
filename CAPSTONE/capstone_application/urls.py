from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("logout",views.logout, name="logout"),
    path("login",views.login_view, name="login"),
    path("register",views.register, name="register"),
    path("logout",views.logout, name="logout"),
]