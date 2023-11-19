from django.contrib import admin
from django.urls import path , include , re_path
from django.conf import settings
from django.conf.urls.static import static
from account.views import Login , register , activate



urlpatterns = [
    path('admin/', admin.site.urls),

    # صفحه اصلی 
    path('', include('MainPage.urls')),
    # صفحه مقالات 
    path('articles/', include('Articles.urls')),
    # صفحه اکانت 
    path('account/', include('account.urls')),

    path("login/", Login.as_view(), name="login"), #در اینجا اور رایت کردیم ، خودمون نوشتیم

    path("register/", register.as_view(), name="register"),
    # url(r'^signup/$', views.signup, name='signup'),

    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate , name='activate'),
    path('activate/<uidb64>/<token>/', activate , name='activate'),

    path('', include('django.contrib.auth.urls')), #لاگ اوت و سایر مباحث ثبت نام در اینجاست

]


# فقط در حالت دیباگ به کار میاد برای فایل میدیاها است
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)