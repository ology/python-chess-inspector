from django.urls import path

from . import views

app_name = "game"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_page, name="login_page"),
]