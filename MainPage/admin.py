from django.contrib import admin
from .models import AlertModelMainPage, BookHomeModelMainPage




# تنظیمات پیغام
class AlertMainPageAdmin(admin.ModelAdmin):
    list_display = ('title_alert' , 'slug_alert', 'status_alert', 'updated_alert', 'created_alert')
    list_filter = (['publish_alert' ,'status_alert'] )
    search_fields = ('title_alert' ,'description_alert'  )
    prepopulated_fields = {'slug_alert': ('title_alert',)}
    ordering = ['-publish_alert' , 'status_alert']

admin.site.register(AlertModelMainPage, AlertMainPageAdmin)
admin.site.title_article = 'مدیریت پیغام ها'
# --------------------------------------------------



# تنظیمات کتاب صفحه اصلی
class BookHomeMainPageAdmin(admin.ModelAdmin):
    list_display = ('title_BookHome' , 'slug_BookHome', 'status_BookHome', 'updated_BookHome', 'created_BookHome')
    list_filter = (['publish_BookHome' ,'status_BookHome'] )
    search_fields = ('title_BookHome' ,'description_BookHome'  )
    prepopulated_fields = {'slug_BookHome': ('title_BookHome',)}
    ordering = ['-publish_BookHome' , 'status_BookHome']

admin.site.register(BookHomeModelMainPage, BookHomeMainPageAdmin)
admin.site.title_article = 'مدیریت کتاب ها'
# --------------------------------------------------
