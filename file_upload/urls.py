from django.urls import path
from . import views
from . import teste
urlpatterns = [
    path("home", views.home, name="home")
]