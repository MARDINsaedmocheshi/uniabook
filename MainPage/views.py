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