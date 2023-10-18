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



# Alert | پیغام
class AlertTop(models.Model):
  STATUS_CHOICES = (
    ('d','پیش نویس'),
    ('p','منتشر'),
    ('f','پیغام فاقد محتوا'),
    ('n','حذف خواهد شد'),
    ('b','به زودی منتشر خواهد شد'),
    ('r','به دلیل عمل نکردن به قوانین سایت رد شد'),
  )
  Alert_CHOICES= [
   ("نوع پیغام", (
           ("hhh", "هشدار"),
           ("sss", "مهم"),
           ("aaa", "پیغام تعمیر"),
           ("qqq", "پیغام اضافه شدن ویژگی جدید"),
           ("www", "پیغام تخفیف ویژه"),
           ("eee", "پیغام کمک"),
           ("rrr", "پیغام اطلاع رسانی"),
           ("ttt", "پیغام انگیزشی"),
           ("yyy", "پیغام تبلیغاتی"),
           ("uuu", "پیغام ارتباط با ما"),
           ("iii", "پیغام تبریک"),
           ("ooo", " سایر "),

       )
   ),
  ]

  image_alert = models.ImageField(null=True,blank=True, upload_to="alert_image", verbose_name = "عکس پیغام")
  title_alert = models.CharField(max_length=200, verbose_name = "عنوان پیغام")
  slug_alert = models.SlugField(max_length=100 , unique=True, verbose_name = "آدرس پیغام")
  category_alert = models.ManyToManyField("Category", verbose_name="دسته بندی", related_name="alerts")
  description_alert = models.TextField(verbose_name = "توضیح کوتاه")
#  description_alert = RichTextField(blank=True, null=True,verbose_name = "توضیح کوتاه")
  publish_alert = models.DateTimeField(default=timezone.now, verbose_name = "زمان انتشار پیغام")
  created_alert = models.DateTimeField(auto_now_add=True, verbose_name = "پیغام کی ایجاد شد؟") 
  updated_alert = models.DateTimeField(auto_now =True, verbose_name = "پیغام کی آپدیت شد؟")
  status_alert = models.CharField(max_length=1,choices=STATUS_CHOICES,default = 'd', verbose_name = "  وضعیت انتشار پیغام" )
  Alert_type_alert = models.CharField(max_length=3,choices=Alert_CHOICES, verbose_name = " نوع پیغام" )
  Emphasis_on_the_message_alert = models.BooleanField(default=False, verbose_name = "تاکید به پیغام")

  class Meta:
    verbose_name_plural = "پیغام ها"
    verbose_name = "پیغام"
    
  def __str__(self):
    return self.title_alert

  def jpublish(self):
      return jalali_convert(self.publish_alert)
  jpublish.short_description ="زمان انتشار"

  def categore_published(self):
    return self.category_alert.filter(status_category=True)

#   objects = AlertManagers()

# ------------------------------------------------------------------------------------------------

# Slider | اسلایدر
class SliderTop(models.Model):
  STATUS_CHOICES = (
    ('d','پیش نویس'),
    ('p','منتشر'),
    ('f','اسلاید فاقد محتوا'),
    ('n','حذف خواهد شد'),
    ('b','به زودی منتشر خواهد شد'),
    ('r','به دلیل عمل نکردن به قوانین سایت رد شد'),
  )
  Slider_CHOICES= [
   ("نوع اسلاید", (
           ("qwe", "تبلیغاتی"),
           ("qwr", "آموزشی"),
           ("qwt", "مقاله برتر"),
           ("qwy", "معرفی کتاب"),
           ("qwu", "معرفی موضوع هفته"),
           ("qwi", "جملات انگیزشی"),
           ("qwo", "معرفی شخص"),
       )
   ),
  ]

  image_alert = models.ImageField(upload_to="Slieder_image", verbose_name = "عکس اسلاید")
  title_Sliedr = models.CharField(max_length=200, verbose_name = "عنوان اسلاید")
  slug_Sliedr = models.SlugField(max_length=100 , unique=True, verbose_name = "آدرس اسلاید")
  category_Sliedr = models.ManyToManyField("Category", verbose_name="دسته بندی", related_name="Sliedrs")
  description_Sliedr = models.TextField(verbose_name = "توضیح کوتاه")
#  description_Sliedr = RichTextField(blank=True, null=True,verbose_name = "توضیح کوتاه")
  publish_Sliedr = models.DateTimeField(default=timezone.now, verbose_name = "زمان انتشار اسلاید")
  created_Sliedr = models.DateTimeField(auto_now_add=True, verbose_name = "اسلاید کی ایجاد شد؟") 
  updated_Sliedr = models.DateTimeField(auto_now =True, verbose_name = "اسلاید کی آپدیت شد؟")
  status_Sliedr = models.CharField(max_length=1,choices=STATUS_CHOICES,default = 'd', verbose_name = "  وضعیت انتشار اسلاید" )
  Sliedr_type_Sliedr = models.CharField(max_length=3,choices=Slider_CHOICES, verbose_name = " نوع اسلاید" )
  Emphasis_on_the_message_Sliedr = models.BooleanField(default=False, verbose_name = "تاکید به اسلاید")

  class Meta:
    verbose_name_plural = "اسلاید ها"
    verbose_name = "اسلاید"
    
  def __str__(self):
    return self.title_Sliedr

  def jpublish(self):
      return jalali_convert(self.publish_Sliedr)
  jpublish.short_description ="زمان انتشار"

  def categore_published(self):
    return self.category_Sliedr.filter(status_category=True)

#   objects = SliedrManagers()

# ------------------------------------------------------------------------------------------------

