from django.urls import path
from .views import Articles_view

app_name = "Articles_app_name"
urlpatterns = [
    path('', Articles_view , name="Articles_name"),
]

