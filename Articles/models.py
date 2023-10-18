from django.db import models
from django.utils import timezone
from extensions.utils import jalali_convert







# Category
class Category(models.Model):
  parent = models.ForeignKey('self',  default=None, null=True,blank=True, on_delete=models.SET_NULL, related_name="children", verbose_name = "دسته بندی والد | زیر دسته")
  title_category = models.CharField(max_length=200, verbose_name = "عنوان دسته بندی ")
  slug_category = models.SlugField(max_length=100 , unique=True, verbose_name = "آدرس دسته بندی")
  status_category = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
  position_category = models.IntegerField(verbose_name="شماره دسته بندی")

  publish_category = models.DateTimeField(default=timezone.now, verbose_name = "زمان انتشار دسته بندی")
  created_category = models.DateTimeField(auto_now_add=True, verbose_name = "دسته بندی کی ایجاد شد؟") 
  updated_category = models.DateTimeField(auto_now =True, verbose_name = "دسته بندی کی آپدیت شد؟")

  class Meta:
    verbose_name ="دسته بندی"
    verbose_name_plural ="دسته بندی ها"
    ordering = ['parent__id','position_category']

  def __str__(self):
    return self.title_category

  def jpublish(self):
      return jalali_convert(self.publish_category)
  jpublish.short_description ="زمان انتشار"

  # objects = CategoryManagers()  
# -----------------------------------------------
