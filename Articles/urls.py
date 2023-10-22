from django.urls import path
from .views import Articles_view , detail_alert , detail_slider , detail_article, category_alert , category_slider , category_article

app_name = "Articles_app_name"
urlpatterns = [
    path('', Articles_view , name="Articles_name"),

    path('category_alert/<slug:slug>', category_alert, name="category_alert_name"),
    path('alert/<slug:slug>', detail_alert, name="alert_name"),

    path('category_slider/<slug:slug>', category_slider, name="category_slider_name"),
    path('slider/<slug:slug>', detail_slider, name="slider_name"),

    path('category_article/<slug:slug>', category_article, name="category_article_name"),
    path('article/<slug:slug>', detail_article, name="article_name"),
]

