from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "todo"
urlpatterns = [
    path('', views.index, name="index"),
]