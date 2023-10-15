from django.urls import path
from .views import MainPage_view, about_view, detail_alert, detail_book, detail_article, category_books

app_name = "MainPage_app_name"
urlpatterns = [
    path('', MainPage_view, name="MainPage_name"),
    path('about/', about_view, name="about_name"),
    path('alert/<slug:slug>', detail_alert, name="alert_name"),
    path('book/<slug:slug>', detail_book, name="book_name"),
    path('article/<slug:slug>', detail_article, name="article_name"),
    path('category/<slug:slug>', category_books , name="category_books_name"),


]

