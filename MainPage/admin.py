from django.contrib import admin
from .models import AlertModelMainPage, BookHomeModelMainPage, ArticleHomeModelMainPage, Category


# تنظیمات دسته بندی
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position_category','title_category', 'slug_category' , 'parent', 'status_category')
    list_filter = (['status_category'])
    search_fields = ('title_category' ,'slug_category')
    prepopulated_fields = {'slug_category': ('title_category',)}

admin.site.register(Category, CategoryAdmin)
admin.site.title_category = 'مدیریت دسته بندی'
# --------------------------------------------------


# تنظیمات پیغام
class AlertMainPageAdmin(admin.ModelAdmin):
    list_display = ('title_alert' , 'slug_alert', 'status_alert', 'jpublish', 'updated_alert', 'created_alert', 'category_to_str')
    list_filter = (['publish_alert' ,'status_alert'] )
    search_fields = ('title_alert' ,'description_alert'  )
    prepopulated_fields = {'slug_alert': ('title_alert',)}
    ordering = ['-publish_alert' , 'status_alert']

    def category_to_str(self, obj):
        return "،".join([category.title_category for category in obj.category_alert.all()])
    category_to_str.short_description ="دسته بندی"

admin.site.register(AlertModelMainPage, AlertMainPageAdmin)
admin.site.title_article = 'مدیریت پیغام ها'
# --------------------------------------------------



# تنظیمات کتاب صفحه اصلی
class BookHomeMainPageAdmin(admin.ModelAdmin):
    list_display = ('title_BookHome' , 'slug_BookHome', 'status_BookHome', 'updated_BookHome', 'created_BookHome', 'category_to_str')
    list_filter = (['publish_BookHome' ,'status_BookHome'] )
    search_fields = ('title_BookHome' ,'description_BookHome'  )
    prepopulated_fields = {'slug_BookHome': ('title_BookHome',)}
    ordering = ['-publish_BookHome' , 'status_BookHome']

    def category_to_str(self, obj):
        return "،".join([category.title_category for category in obj.category_BookHome.all()])
    category_to_str.short_description ="دسته بندی"


admin.site.register(BookHomeModelMainPage, BookHomeMainPageAdmin)
admin.site.title_article = 'مدیریت کتاب ها'
# --------------------------------------------------


# تنظیمات مقاله صفحه اصلی
class ArticleHomeMainPageAdmin(admin.ModelAdmin):
    list_display = ('title_ArticleHome' , 'slug_ArticleHome', 'status_ArticleHome', 'updated_ArticleHome', 'created_ArticleHome')
    list_filter = (['publish_ArticleHome' ,'status_ArticleHome'] )
    search_fields = ('title_ArticleHome' ,'Body_or_text_ArticleHome'  )
    prepopulated_fields = {'slug_ArticleHome': ('title_ArticleHome',)}
    ordering = ['-publish_ArticleHome' , 'status_ArticleHome']

admin.site.register(ArticleHomeModelMainPage, ArticleHomeMainPageAdmin)
admin.site.title_article = 'مدیریت کتاب ها'
# --------------------------------------------------
