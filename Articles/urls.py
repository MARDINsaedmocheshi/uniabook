from django.urls import path
from .views import Articles_view , detail_alert

app_name = "Articles_app_name"
urlpatterns = [
    path('', Articles_view , name="Articles_name"),
    path('alert/<slug:slug>', detail_alert, name="alert_name"),
]

