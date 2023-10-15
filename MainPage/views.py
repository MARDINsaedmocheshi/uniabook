from django.shortcuts import render
from .models import AlertModelMainPage, BookHomeModelMainPage, ArticleHomeModelMainPage, Category

def MainPage_view(request):
    cotext = {

        # پیغام ها
         "Alertspagemain" : AlertModelMainPage.objects.filter(status_alert="p"), # شیش تای آخر رو نشون میده
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
        "category" : Category.objects.filter(status_category=True)
    }
    return render(request, "MainPage/alert_detail.html", cotext)
# -----------------------------------------------


# صحفه لینک مربوطه هر کتاب
def detail_book(request, slug):
    cotext = {
        # کتاب ها 
        "Bookspagemain" : BookHomeModelMainPage.objects.filter(status_BookHome="p")[:6],
        "detail_book" : BookHomeModelMainPage.objects.get(slug_BookHome=slug),
        "category" : Category.objects.filter(status_category=True)
    }
    return render(request, "MainPage/book_detail.html", cotext)
# -----------------------------------------------


# صحفه لینک مربوطه هر مقاله
def detail_article(request, slug):
    cotext = {
        # مقاله ها     
        "Articlspagemain" : ArticleHomeModelMainPage.objects.filter(status_ArticleHome="p")[:6],
        "detail_article" : ArticleHomeModelMainPage.objects.get(slug_ArticleHome=slug),
        "category" : Category.objects.filter(status_category=True)
    }
    return render(request, "MainPage/article_detail.html", cotext)
# -----------------------------------------------
