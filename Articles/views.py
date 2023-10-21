from django.shortcuts import render, get_object_or_404
from .models import Category , AlertTop , SliderTop , ArticlesModel

# مربوط به صفحه مقالات
def Articles_view(request):
    cotext = {

        # دسته بندی ها
         "CATEGORY" : Category.objects.filter(status_category=True),
        # پیغام ها
         "ALERT" : AlertTop.objects.filter(status_alert="p"),
        # اسلایدر ها
         "SLIDER" : SliderTop.objects.filter(status_Sliedr="p")[:3],
        # مقاله ها
         "ARTICLE" : ArticlesModel.objects.filter(status_Article="p")[:6],

     }
    return render(request, "Articles/index_Articles.html", cotext)
# -----------------------------------------------


# صحفه  مربوطه هر پیغام
def detail_alert(request, slug):
    cotext = {
        # پیغام ها
        "detail_alert" :  get_object_or_404(AlertTop , slug_alert=slug)
       
    }
    return render(request, "Articles/detail_alert.html", cotext)
# -----------------------------------------------





# صحفه  مربوطه هر اسلایدر
def detail_slider(request, slug):
    cotext = {
        # پیغام ها
        "detail_slider" : get_object_or_404(SliderTop , slug_Sliedr=slug)
    }
    return render(request, "Articles/detail_slider.html", cotext)
# -----------------------------------------------







# صحفه  مربوطه هر مقاله
def detail_article(request, slug):
    cotext = {
        # پیغام ها
        "detail_article" : get_object_or_404(ArticlesModel , slug_Article=slug)
    }
    return render(request, "Articles/detail_article.html", cotext)
# -----------------------------------------------
