from django.shortcuts import render, get_object_or_404
from .models import Category , AlertTop , SliderTop , ArticlesModel
from django.core.paginator import Paginator
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from account.models import User
# from .forms import ArticlesModelForm
from account.mixins import AuthorAccessMixin
# from django.db.models import Count , Q
# from datetime import datetime , timedelta



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
    paginate_by = 5

    # def get_context_data(self, **kwargs):
        # last_month = datetime.today() - timedelta(days=30)
        # context = super().get_context_data(**kwargs)
        # context["popular_articles"] =  #در فایل تمپلت تگها
        # return context


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
class category_article(ListView):
    paginate_by = 3
    template_name = "Articles/category_article.html"

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category , slug_category=slug , status_category=True)
        # category = get_object_or_404(Category.objects.active() , slug_category=slug)
        return category.articls.published()

    def get_context_data(self, **kwargs):
        # slug = self.kwargs.get('slug')
        context = super().get_context_data(**kwargs)
        # context["category"] = get_object_or_404(Category, slug_category=slug , status_category=True)
        context["category"] = category
        return context

# صحفه دسته بندی مربوطه هر مقاله
# def category_article(request, slug , page=1):
#     category = get_object_or_404(Category , slug_category=slug , status_category=True)
#     Article_list = category.articls.published()

#     paginator = Paginator(Article_list, 3)
#     articls = paginator.get_page(page)

#     cotext = {
        
#         # "category" :  get_object_or_404(Category , slug_category=slug , status_category=True)
#         "category" : category,
#         "articls" :  articls,
       
#     }
#     return render(request, "Articles/category_article.html", cotext)
# -----------------------------------------------
# صحفه  مربوطه هر مقاله
# def detail_article(request, slug):
#     cotext = {
#         # مقاله ها
#         "detail_article" : get_object_or_404(ArticlesModel , slug_Article=slug , status_Article="p"),
#         # دسته بندی ها
#         # "CATEGORY" : Category.objects.filter(status_category=True),

#     }
#     return render(request, "Articles/detail_article.html", cotext)
# -----------------------------------------------
# صحفه  مربوطه هر مقاله
class detail_article(DetailView):
    template_name = "Articles/detail_article.html"
    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(ArticlesModel , slug_Article=slug , status_Article="p")

        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all() :
            article.hits.add(ip_address)

        return article



# صحفه  مربوطه هر مقاله وقتی پیش نویس است برای ادمین ها نمایش داده شود
class detail_article_preview(AuthorAccessMixin , DetailView):
    template_name = "Articles/detail_article.html"
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(ArticlesModel , pk=pk )





# -----------------------------------------------
class AuthorList(ListView):
    paginate_by = 2
    template_name = "Articles/author_list.html"

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articls.published()

    def get_context_data(self, **kwargs):
        # slug = self.kwargs.get('slug')
        context = super().get_context_data(**kwargs)
        # context["auther"] = get_object_or_404(auther.objects.active(), slug_category=slug)
        context["author"] = author
        return context
