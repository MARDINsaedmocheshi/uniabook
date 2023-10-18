from django.shortcuts import render, get_object_or_404
from .models import Category , AlertTop , SliderTop , ArticlesModel


def Articles_view(request):
    cotext = {

        # دسته بندی ها
         "CATEGORY" : Category.objects.filter(status_category=True),
        # پیغام ها
         "ALERT" : AlertTop.objects.filter(status_alert="p"),
        #  "Alertspagemain" : AlertModelMainPage.objects.published(), # میتونی اینجوری هم بنویسی
        # اسلایدر ها
         "SLIDER" : SliderTop.objects.filter(status_Sliedr="p")[:3],
        # مقاله ها
         "ARTICLE" : ArticlesModel.objects.filter(status_Article="p")[:6],

     }
    return render(request, "Articles/index_Articles.html", cotext)
# -----------------------------------------------
