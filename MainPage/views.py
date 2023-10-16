from django.shortcuts import render, get_object_or_404
from .models import AlertModelMainPage, BookHomeModelMainPage, ArticleHomeModelMainPage, Category

def MainPage_view(request):
    cotext = {

        # پیغام ها
         "Alertspagemain" : AlertModelMainPage.objects.filter(status_alert="p"), # شیش تای آخر رو نشون میده
        #  "Alertspagemain" : AlertModelMainPage.objects.published(), # میتونی اینجوری هم بنویسی
        # کتاب ها        
         "Bookspagemain" : BookHomeModelMainPage.objects.filter(status_BookHome="p")[:6], # شیش تای آخر رو نشون میده
        # مقاله ها        
         "Articlspagemain" : ArticleHomeModelMainPage.objects.filter(status_ArticleHome="p")[:6], # شیش تای آخر رو نشون میده

     }
    return render(request, "MainPage/index.html", cotext)
# -----------------------------------------------


# صفحه ما کی هستیم؟
def about_view(request):
    cotext = {
        # پیغام ها
         "Alertspagemain" : AlertModelMainPage.objects.filter(status_alert="p"),
         
     }
    return render(request, "MainPage/about.html", cotext)
# -----------------------------------------------


# صحفه لینک مربوطه هر پیغام
def detail_alert(request, slug):
    cotext = {
        # پیغام ها
        "Alertspagemain" : AlertModelMainPage.objects.filter(status_alert="p"),
        "detail_alert" : AlertModelMainPage.objects.get(slug_alert=slug),
        "category" : Category.objects.filter(status_category=True),
        "DA" : get_object_or_404(AlertModelMainPage , slug_alert=slug , status_alert="p")
        # "DA" : get_object_or_404(AlertModelMainPage.objects.published() , slug_alert=slug)# میتونی اینجوری هم بنویسی
    }
    return render(request, "MainPage/alert_detail.html", cotext)
# -----------------------------------------------


# صحفه لینک مربوطه هر کتاب
def detail_book(request, slug):
    cotext = {
        # کتاب ها 
        "Bookspagemain" : BookHomeModelMainPage.objects.filter(status_BookHome="p")[:6],
        "detail_book" : BookHomeModelMainPage.objects.get(slug_BookHome=slug),
        "category" : Category.objects.filter(status_category=True),
        "DB" : get_object_or_404(BookHomeModelMainPage , slug_BookHome=slug , status_BookHome="p")
    }
    return render(request, "MainPage/book_detail.html", cotext)
# -----------------------------------------------


# صحفه لینک مربوطه هر مقاله
def detail_article(request, slug):
    cotext = {
        # مقاله ها     
        "Articlspagemain" : ArticleHomeModelMainPage.objects.filter(status_ArticleHome="p")[:6],
        "detail_article" : ArticleHomeModelMainPage.objects.get(slug_ArticleHome=slug),
        "category" : Category.objects.filter(status_category=True),
        "DAR" : get_object_or_404(ArticleHomeModelMainPage , slug_ArticleHome=slug , status_ArticleHome="p")
    }
    return render(request, "MainPage/article_detail.html", cotext)
# -----------------------------------------------



def category_Alert(request, slug):
    cotext = {
        # دسته بندی ها
        "category" : get_object_or_404(Category, slug_category=slug, status_category=True),
        # "category" : get_object_or_404(Category.objects.published(), slug_category=slug),# میتونی اینجوری هم بنویسی
        # "category1" : Category.objects.filter(status_category=True)
    }
    return render(request, "MainPage/category_alerts.html", cotext)
# -----------------------------------------------



def category_books(request, slug):
    cotext = {
        # دسته بندی ها
        "category" : get_object_or_404(Category, slug_category=slug, status_category=True),
        # "category1" : Category.objects.filter(status_category=True)
    }
    return render(request, "MainPage/category_books.html", cotext)
# -----------------------------------------------

def category_Articls(request, slug):
    cotext = {
        # دسته بندی ها
        "category" : get_object_or_404(Category, slug_category=slug, status_category=True),
        # "category1" : Category.objects.filter(status_category=True)
    }
    return render(request, "MainPage/category_Articls.html", cotext)
# -----------------------------------------------

