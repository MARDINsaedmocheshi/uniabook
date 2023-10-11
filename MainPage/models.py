from django.db import models
from django.utils import timezone













# Alert | پیغام
class AlertModelMainPage(models.Model):
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

  title_alert = models.CharField(max_length=200, verbose_name = "عنوان پیغام")
  slug_alert = models.SlugField(max_length=100 , unique=True, verbose_name = "آدرس پیغام")
#   category_alert = models.ManyToManyField("Category", verbose_name="دسته بندی", related_name="articls")
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


# ------------------------------------------------------------------------------------------------


# Home page book | کتاب صفحه اصلی 
class BookHomeModelMainPage(models.Model):
  STATUS_CHOICES = (
    ('d','پیش نویس'),
    ('p','منتشر'),
    ('p','تعداد کتاب محدود'),
    ('f','کتاب موجود نیست'),
    ('n','حذف خواهد شد'),
    ('b','به زودی موجود خواهد شد'),
    ('r','به دلیل عمل نکردن به قوانین سایت رد شد'),
  )
  BookHome_CHOICES= [
   ("انواع کتاب بر اساس موضوع؛ انواع سبک کتاب", (

           ("ban", "دانشگاهی"),
           ("bao", "آموزشی"), 
           ("bab", "فانتزی"),
           ("bac", "ماجراجویی"),
           ("bad", "عاشقانه "),
           ("bae", "ترسناک"),
           ("baf", "مهیج "),
           ("bag", "علمی تخیلی"),
           ("bah", "هنری"),
           ("bai", "انگیزشی"),
           ("baj", "طنز"),
           ("bak", "کودکان"),
           ("bal", "کتاب های زندگینامه"),
           ("bam", "کتاب های سفرنامه"),


       )
   ),
  ]

  image_BookHome = models.ImageField(upload_to="BookHome_image", verbose_name = "عکس کتاب")
  title_BookHome = models.CharField(max_length=200, verbose_name = "نام کتاب به طور کامل" )
  slug_BookHome = models.SlugField(max_length=100 , unique=True, verbose_name = "آدرس کتاب")
#   نام نویسنده
  Publication_name_BookHome = models.CharField(max_length=200, verbose_name = "نام نشر" )
  publication_date_BookHome = models.CharField(max_length=200, verbose_name = "تاریخ نشر" )
  Place_of_publication_BookHome = models.CharField(max_length=200, verbose_name = "محل نشر" )
  name_of_the_printing_house_BookHome = models.CharField(max_length=200, verbose_name = "نام چاپخانه" )
  Number_of_circulation_BookHome = models.CharField(max_length=200, verbose_name = "تعداد تیراژ" )
  Publishedbook_BookHome = models.CharField(max_length=200, verbose_name = "نوبت چاپ" )
  price_of_the_book_BookHome = models.DecimalField(default=0, max_digits=12, decimal_places=0, verbose_name = "قیمت کتاب")
  name_of_the_translator_or_translators_BookHome = models.CharField(max_length=200, verbose_name = "نام مترجم یا مترجمان" )
#   category_BookHome = models.ManyToManyField("Category", verbose_name="دسته بندی", related_name="articls")
  description_BookHome = models.TextField(verbose_name = "توضیحات کتاب")
#  description_BookHome = RichTextField(blank=True, null=True,verbose_name = "توضیح کوتاه")
  publish_BookHome = models.DateTimeField(default=timezone.now, verbose_name = "زمان انتشار کتاب")
  created_BookHome = models.DateTimeField(auto_now_add=True, verbose_name = "کتاب کی ایجاد شد؟") 
  updated_BookHome = models.DateTimeField(auto_now =True, verbose_name = "کتاب کی آپدیت شد؟")
  status_BookHome = models.CharField(max_length=1,choices=STATUS_CHOICES,default = 'd', verbose_name = "  وضعیت انتشار کتاب" )
  BookHome_type_BookHome = models.CharField(max_length=3,choices=BookHome_CHOICES, verbose_name = " نوع کتاب" )
  is_sale_BookHome = models.BooleanField(default=False, verbose_name = "تخفیف ویژه")

  class Meta:
    verbose_name_plural = "کتاب ها"
    verbose_name = "کتاب"
    
  def __str__(self):
    return self.title_BookHome


# ------------------------------------------------------------------------------------------------

# Home page article | مقاله صفحه اصلی 
class ArticleHomeModelMainPage(models.Model):
  STATUS_CHOICES = (
    ('d','پیش نویس'),
    ('p','منتشر'),
    ('p','تعداد کتاب محدود'),
    ('f','کتاب موجود نیست'),
    ('n','حذف خواهد شد'),
    ('b','به زودی موجود خواهد شد'),
    ('r','به دلیل عمل نکردن به قوانین سایت رد شد'),
  )
  ArticleHome_CHOICES= [
   ("نوع مقاله", (
           ("sar", "سایر"),
           ("dns", "دانشجویی"),
           ("ora", "مقاله پژوهشی"),
           ("taa", "مقاله نظری"),
           ("dor", "روش تحقیق"),
           ("brr", "نقد کتاب"),
           ("isi", "مقالات ISI"),
           ("isc", "مقالات ISC"),
           ("ara", "مقالات مروری"),
           ("dst", "نوشته روزانه"),
           ("cof", "مقالات کنفرانسی"),
           ("scs", "مقالات اسکوپوس"),
           ("rso", "گزارش‌ها و مطالعه مشاهدات"),
           ("ass", "گزارش‌ها یا نامه‌های کوتاه"),


       )
   ),
  ]

  image_ArticleHome = models.ImageField(upload_to="ArticleHome_image", verbose_name = "عکس مقاله")
  File_ArticleHome = models.FileField(upload_to="ArticleHome_file", verbose_name = "فایل مقاله")
  title_ArticleHome = models.CharField(max_length=200, verbose_name = "نام مقاله" )
  slug_ArticleHome = models.SlugField(max_length=100 , unique=True, verbose_name = "آدرس مقاله")
#   نام مولف یا مولفان
  Abstract_ArticleHome = models.TextField(verbose_name = "چکیده")
  Key_word_ArticleHome = models.CharField(max_length=200, verbose_name = "کلید واژه" )
  Introduction_ArticleHome = models.TextField(verbose_name = "مقدمه")
  Body_or_text_ArticleHome = models.TextField(verbose_name = "بدنه یا متن")
  Result_ArticleHome = models.TextField(verbose_name = "نتیجه")
  References_ArticleHome = models.CharField(max_length=200, verbose_name = "منابع و ماخذ" )
#   category_ArticleHome = models.ManyToManyField("Category", verbose_name="دسته بندی", related_name="articls")
#  description_ArticleHome = RichTextField(blank=True, null=True,verbose_name = "توضیح کوتاه")
  publish_ArticleHome = models.DateTimeField(default=timezone.now, verbose_name = "زمان انتشار مقاله")
  created_ArticleHome = models.DateTimeField(auto_now_add=True, verbose_name = "مقاله کی ایجاد شد؟") 
  updated_ArticleHome = models.DateTimeField(auto_now =True, verbose_name = "مقاله کی آپدیت شد؟")
  status_ArticleHome = models.CharField(max_length=1,choices=STATUS_CHOICES,default = 'd', verbose_name = "  وضعیت انتشار مقاله" )
  ArticleHome_type_ArticleHome = models.CharField(max_length=3,choices=ArticleHome_CHOICES, verbose_name = " نوع مقاله" )
  is_sale_ArticleHome = models.BooleanField(default=False, verbose_name = "تخفیف ویژه")

  class Meta:
    verbose_name_plural = "مقاله ها"
    verbose_name = "مقاله"
    
  def __str__(self):
    return self.title_ArticleHome


# ------------------------------------------------------------------------------------------------

