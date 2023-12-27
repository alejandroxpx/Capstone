from django.urls import path
from django.conf import settings
# from django.views.generic import RedirectView
# from django.conf.urls import url
# from django.conf.urls.static import static
from . import views 

urlpatterns = [
    path("", views.index, name = "index"),
    path("login",views.login_view, name="login"),
    path("logout",views.logout, name="logout"),
    path("register",views.register, name="register"),
    path("mercury",views.mercury, name="mercury"),
    path("venus",views.venus, name="venus"),
    path("earth",views.earth, name="earth"),
    path("mars",views.mars, name="mars"),
    path("jupiter",views.jupiter, name="jupiter"),
    path("saturn",views.saturn, name="saturn"),
    path("uranus",views.uranus, name="uranus"),
    path("neptune",views.neptune, name="neptune"),
    # path("login",views.login, name="login"),
    path("logout",views.logout, name="logout")

]