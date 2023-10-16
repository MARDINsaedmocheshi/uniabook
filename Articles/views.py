from django.shortcuts import render, get_object_or_404
# from .models import 

def Articles_view(request):
    # cotext = {

    #     # پیغام ها
    #      "Alertspagemain" : AlertModelMainPage.objects.filter(status_alert="p"), # شیش تای آخر رو نشون میده
    #     #  "Alertspagemain" : AlertModelMainPage.objects.published(), # میتونی اینجوری هم بنویسی
    #     # کتاب ها        
    #      "Bookspagemain" : BookHomeModelMainPage.objects.filter(status_BookHome="p")[:6], # شیش تای آخر رو نشون میده
    #     # مقاله ها        
    #      "Articlspagemain" : ArticleHomeModelMainPage.objects.filter(status_ArticleHome="p")[:6], # شیش تای آخر رو نشون میده

    #  }
    return render(request, "Articles/index_Articles.html")
    # return render(request, "MainPage/index.html", cotext)
# -----------------------------------------------
