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
        # میتونی از هر دوتاش استفاده کنی
        #  "ARTICLE" : ArticlesModel.objects.filter(status_Article="p").order_by('-publish_Article')[:6],
         "ARTICLE" : ArticlesModel.objects.published().order_by('-publish_Article')[:6],

     }
    return render(request, "Articles/index_Articles.html", cotext)
# -----------------------------------------------






# صحفه دسته بندی مربوطه هر پیغام
def category_alert(request, slug):
    cotext = {
        
        "category" :  get_object_or_404(Category , slug_category=slug , status_category=True)
       
    }
    return render(request, "Articles/category_alert.html", cotext)
# -----------------------------------------------
# صحفه  مربوطه هر پیغام
def detail_alert(request, slug):
    cotext = {
        # پیغام ها
        "detail_alert" :  get_object_or_404(AlertTop , slug_alert=slug , status_alert="p")
       
    }
    return render(request, "Articles/detail_alert.html", cotext)
# -----------------------------------------------




# صحفه دسته بندی مربوطه هر اسلایدر
def category_slider(request, slug):
    cotext = {
        
        "category" :  get_object_or_404(Category , slug_category=slug , status_category=True)
       
    }
    return render(request, "Articles/category_slider.html", cotext)
# -----------------------------------------------
# صحفه  مربوطه هر اسلایدر
def detail_slider(request, slug):
    cotext = {
        # پیغام ها
        "detail_slider" : get_object_or_404(SliderTop , slug_Sliedr=slug , status_Sliedr="p")
    }
    return render(request, "Articles/detail_slider.html", cotext)
# -----------------------------------------------






# صحفه دسته بندی مربوطه هر مقاله
def category_article(request, slug):
    cotext = {
        
        "category" :  get_object_or_404(Category , slug_category=slug , status_category=True)
       
    }
    return render(request, "Articles/category_article.html", cotext)
# -----------------------------------------------
# صحفه  مربوطه هر مقاله
def detail_article(request, slug):
    cotext = {
        # مقاله ها
        "detail_article" : get_object_or_404(ArticlesModel , slug_Article=slug , status_Article="p"),
        # دسته بندی ها
        # "CATEGORY" : Category.objects.filter(status_category=True),

    }
    return render(request, "Articles/detail_article.html", cotext)
# -----------------------------------------------
