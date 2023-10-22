from django.urls import path
from .views import Articles_view , detail_alert , detail_slider , detail_article, category_alert

app_name = "Articles_app_name"
urlpatterns = [
    path('', Articles_view , name="Articles_name"),

    path('category_alert/<slug:slug>', category_alert, name="category_alert_name"),
    path('alert/<slug:slug>', detail_alert, name="alert_name"),

    # path('category_alert/<slug:slug>', category_alert, name="category_alert_name"),
    path('slider/<slug:slug>', detail_slider, name="slider_name"),

    path('article/<slug:slug>', detail_article, name="article_name"),
]

