from django.urls import path
from .views import Articles_view , detail_alert , detail_slider , detail_article, category_alert , category_slider , category_article , AuthorList , detail_article_preview, SearchList

app_name = "Articles_app_name"
urlpatterns = [
    path('', Articles_view.as_view() , name="Articles_name"),
    path('article/<int:page>', Articles_view.as_view() , name="Articles_name"),

    path('category_alert/<slug:slug>', category_alert, name="category_alert_name"),
    path('alert/<slug:slug>', detail_alert, name="alert_name"),

    path('category_slider/<slug:slug>', category_slider, name="category_slider_name"),
    path('slider/<slug:slug>', detail_slider, name="slider_name"),

    path('category_article/<slug:slug>', category_article.as_view(), name="category_article_name"),
    path('category_article/<slug:slug>/<int:page>', category_article.as_view(), name="category_article_name"),
    path('article/<slug:slug>', detail_article.as_view(), name="article_name"),
    path('preview/<int:pk>', detail_article_preview.as_view(), name="article_preview"),


    path('author/<slug:username>', AuthorList.as_view() , name="author_article_name"),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view() , name="author_article_name"),

    path('search/', SearchList.as_view() , name="search"),
    path('search/page/<int:page>', SearchList.as_view() , name="search"),

]


