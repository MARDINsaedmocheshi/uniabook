from django.contrib import admin
from .models import Category


# تنظیمات دسته بندی
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position_category','title_category', 'slug_category' , 'parent', 'status_category','jpublish','created_category','updated_category')
    list_filter = (['status_category'])
    search_fields = ('title_category' ,'slug_category')
    prepopulated_fields = {'slug_category': ('title_category',)}

admin.site.register(Category, CategoryAdmin)
admin.site.title_category = 'مدیریت دسته بندی'
# --------------------------------------------------
