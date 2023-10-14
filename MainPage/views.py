from django.shortcuts import render
from .models import AlertModelMainPage, BookHomeModelMainPage, ArticleHomeModelMainPage

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


# صفحه ما کی هستیم؟
def about_view(request):
    cotext = {
        # پیغام ها
         "Alertspagemain" : AlertModelMainPage.objects.filter(status_alert="p"), # شیش تای آخر رو نشون میده
     }
    return render(request, "MainPage/about.html", cotext)


# صحفه لینک مربوطه هر پیغام
def detail_alert(request, slug):
    cotext = {
        "detail_alert" : AlertModelMainPage.objects.get(slug_alert=slug)
    }
    return render(request, "MainPage/alert_detail.html", cotext)
