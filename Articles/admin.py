from django.contrib import admin
from .models import Category , AlertTop


# تنظیمات دسته بندی
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position_category','title_category', 'slug_category' , 'parent', 'status_category','jpublish','created_category','updated_category')
    list_filter = (['status_category'])
    search_fields = ('title_category' ,'slug_category')
    prepopulated_fields = {'slug_category': ('title_category',)}

admin.site.register(Category, CategoryAdmin)
admin.site.title_category = 'مدیریت دسته بندی'
# --------------------------------------------------





# تنظیمات پیغام
class AlertAdmin(admin.ModelAdmin):
    list_display = ('title_alert' , 'slug_alert', 'status_alert', 'jpublish', 'updated_alert', 'created_alert', 'category_to_str')
    list_filter = (['publish_alert' ,'status_alert'] )
    search_fields = ('title_alert' ,'description_alert'  )
    prepopulated_fields = {'slug_alert': ('title_alert',)}
    ordering = ['-publish_alert' , 'status_alert']

    def category_to_str(self, obj):
        return "،".join([category.title_category for category in obj.categore_published()])
    category_to_str.short_description ="دسته بندی"

admin.site.register(AlertTop, AlertAdmin)
admin.site.title_article = 'مدیریت پیغام ها'
# --------------------------------------------------





