from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # صفحه اصلی 
    path('', include('MainPage.urls')),
    # صفحه مقالات 
    path('articles/', include('Articles.urls')),
    # صفحه اکانت 
    path('account/', include('account.urls')),
]


# فقط در حالت دیباگ به کار میاد برای فایل میدیاها است
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)