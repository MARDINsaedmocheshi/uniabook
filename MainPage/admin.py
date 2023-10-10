from django.contrib import admin
from .models import AlertModelMainPage




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
