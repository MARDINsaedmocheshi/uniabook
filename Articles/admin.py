from django.contrib import admin
from .models import Category , AlertTop , SliderTop , ArticlesModel





# غیر فعال کردن بخش حذف مقاله
# admin.site.disable_action("delete_selected")

# اکشن ها
# پیش نویس---------------------------------------------
@admin.action(description="پیش نویس مقالات انتخاب شده")
def make_draft(self, request, queryset):
    rows_updated = queryset.update(status_Article="d")
    if rows_updated == 1:
        message_bit = "پیش نویس شد"
    else:
        message_bit = "پیش نویس شدند."
    self.message_user(request, "{} مقاله {} ".format(rows_updated, message_bit))

#  منتشر ---------------------------------------------
@admin.action(description="انتشار مقالات انتخاب شده")
def make_published(self, request, queryset):
    rows_updated = queryset.update(status_Article="p")
    if rows_updated == 1:
        message_bit = "منتشر شد"
    else:
        message_bit = "منتشر شدند."
    self.message_user(request, "{} مقاله {} ".format(rows_updated, message_bit))


#  رد قانونی ---------------------------------------------
@admin.action(description="به دلیل عمل نکردن به قوانین سایت رد شد")
def make_radq(self, request, queryset):
    rows_updated = queryset.update(status_Article="r")
    if rows_updated == 1:
        message_bit = "رد قانون شد"
    else:
        message_bit = "رد قانون شدند."
    self.message_user(request, "{} مقاله {} ".format(rows_updated, message_bit))
























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
admin.site.title_alert = 'مدیریت پیغام ها'
# --------------------------------------------------





# تنظیمات اسلایدر
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title_Sliedr' , 'slug_Sliedr', 'status_Sliedr', 'jpublish', 'updated_Sliedr', 'created_Sliedr', 'category_to_str' ,'Sliedr_type_Sliedr')
    list_filter = (['publish_Sliedr' ,'status_Sliedr'] )
    search_fields = ('title_Sliedr' ,'description_Sliedr'  )
    prepopulated_fields = {'slug_Sliedr': ('title_Sliedr',)}
    ordering = ['-publish_Sliedr' , 'status_Sliedr']

    def category_to_str(self, obj):
        return "،".join([category.title_category for category in obj.categore_published()])
    category_to_str.short_description ="دسته بندی"

admin.site.register(SliderTop, SliderAdmin)
admin.site.title_Sliedr = 'مدیریت پیغام ها'
# --------------------------------------------------





# تنظیمات مقالات 
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title_Article' , 'slug_Article', 'status_Article', 'jpublish' , 'updated_Article', 'created_Article', 'category_to_str')
    list_filter = (['publish_Article' ,'status_Article'] )
    search_fields = ('title_Article' ,'Body_or_text_Article'  )
    prepopulated_fields = {'slug_Article': ('title_Article',)}
    ordering = ['-publish_Article' , 'status_Article']
    actions = [make_published, make_draft, make_radq]

    def category_to_str(self, obj):
        return "،".join([category.title_category for category in obj.categore_published()])
    category_to_str.short_description ="دسته بندی"


admin.site.register(ArticlesModel, ArticlesAdmin)
admin.site.title_Article = 'مدیریت  مقاله ها'
# --------------------------------------------------
