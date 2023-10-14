from django.urls import path
from .views import MainPage_view, about_view, detail_alert, detail_book

app_name = "MainPage_app_name"
urlpatterns = [
    path('', MainPage_view, name="MainPage_name"),
    path('about/', about_view, name="about_name"),
    path('<slug:slug>', detail_alert, name="alert_name"),
    path('book/<slug:slug>', detail_book, name="book_name"),

]

