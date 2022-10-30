from django.urls import path
from django.conf import settings
# from django.views.generic import RedirectView
# from django.conf.urls import url
# from django.conf.urls.static import static
from . import views 

urlpatterns = [
    path("", views.index, name = "index"),
    path("logout",views.logout, name="logout"),
    path("login",views.login_view, name="login"),
    path("register",views.register, name="register"),
    path("logout",views.logout, name="logout"),
    path("home",views.home, name="home"),
    path("lost",views.lost, name="lost"),
    path("homeless",views.homeless, name="homeless"),
    path("stories",views.stories, name="stories"),
    # url(r'^favicon\.ico$',RedirectView.as_view(url="/static/images/favicon.ico")),
]