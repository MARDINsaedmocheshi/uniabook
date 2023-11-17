from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from account.views import Login



urlpatterns = [
    path('admin/', admin.site.urls),

    # صفحه اصلی 
    path('', include('MainPage.urls')),
    # صفحه مقالات 
    path('articles/', include('Articles.urls')),
    # صفحه اکانت 
    path('account/', include('account.urls')),

    path("login/", Login.as_view(), name="login"), #در اینجا اور رایت کردیم ، خودمون نوشتیم

    path('', include('django.contrib.auth.urls')), #لاگ اوت و سایر مباحث ثبت نام در اینجاست

]


# فقط در حالت دیباگ به کار میاد برای فایل میدیاها است
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)