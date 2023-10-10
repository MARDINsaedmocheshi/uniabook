from django.shortcuts import render

def MainPage_view(request):
    # صفحه اصلی 
    return render(request, "MainPage/index.html")