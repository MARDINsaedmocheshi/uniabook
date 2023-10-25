from django.shortcuts import render, get_object_or_404
from .models import Category , AlertTop , SliderTop , ArticlesModel
from django.core.paginator import Paginator
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView






# class Articles_view(TemplateView):
#     template_name = "Articles/index_Articles.html"
#     paginate_by = 2

#     def get_context_data(self, **kwargs) :
#         context = super(Articles_view , self).get_context_data(**kwargs)
#         context["ARTICLE"] = ArticlesModel.objects.published().order_by('-publish_Article')

#         return context

# مربوط به صفحه مقالات
# def Articles_view(request , page=1):

#     Article_list = ArticlesModel.objects.published().order_by('-publish_Article')
#     paginator = Paginator(Article_list, 2)
#     # page = request.GET.get('page')
#     articls = paginator.get_page(page)

#     cotext = {

#         # دسته بندی ها
#          "CATEGORY" : Category.objects.filter(status_category=True),
#         # پیغام ها
#          "ALERT" : AlertTop.objects.filter(status_alert="p"),
#         # اسلایدر ها
#          "SLIDER" : SliderTop.objects.filter(status_Sliedr="p")[:3],
#         # مقاله ها
#         # میتونی از هر دوتاش استفاده کنی
#         #  "ARTICLE" : ArticlesModel.objects.filter(status_Article="p").order_by('-publish_Article')[:6],
#         #  "ARTICLE" : ArticlesModel.objects.published().order_by('-publish_Article')[:2],
#          "ARTICLE" : articls ,

#      }
#     return render(request, "Articles/index_Articles.html", cotext)
# -----------------------------------------------
class Articles_view(ListView):
    queryset = ArticlesModel.objects.published().order_by('-publish_Article')
    paginate_by = 2

# ------------------------------------------






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
def category_article(request, slug , page=1):
    category = get_object_or_404(Category , slug_category=slug , status_category=True)
    Article_list = category.articls.published()

    paginator = Paginator(Article_list, 3)
    articls = paginator.get_page(page)

    cotext = {
        
        # "category" :  get_object_or_404(Category , slug_category=slug , status_category=True)
        "category" : category,
        "articls" :  articls,
       
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
