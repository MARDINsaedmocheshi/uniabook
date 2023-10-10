from django.urls import path
from .views import MainPage_view

app_name = "MainPage_app_name"
urlpatterns = [
    path('', MainPage_view, name="MainPage_name"),

]

