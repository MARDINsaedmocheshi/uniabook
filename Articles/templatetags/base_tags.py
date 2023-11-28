from django import template
from ..models import Category , ArticlesModel
from django.db.models import Count , Q
from datetime import datetime , timedelta
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.simple_tag
def Title(data= "دانشگاه کتاب و مقاله"):     # این یک مقدار پیش فرض یا دیفالت است که اگر چیزی ننویسیم همین را برمیگرداند 
    return data


@register.inclusion_tag("Articles/partials/category_navbar.html")
def category_navbar():# توی فایل index_Articles.html خط 324 ازش استفاده کرده ام
    return {
        # دسته بندی ها
         "CATEGORY" : Category.objects.filter(status_category=True),

    }

@register.inclusion_tag("registration/partials/link.html")
def link(request, link_name , content , classes):
    return {
        # مربوط به اکتیو بودن منوها
         "request" : request,
         "link_name" : link_name ,
         "link" :  "ACCOUNT:{}".format(link_name),
         "content" : content,
         "classes" : classes,

    }




@register.inclusion_tag("registration/partials/sidebar.html")
def popular_articles(): # توی فایل sidebar.html   ازش استفاده کرده ام
    last_month = datetime.today() - timedelta(days=30)
    return {
        # دسته بندی ها
         "articles" : ArticlesModel.objects.published().order_by('-publish_Article').annotate(count=Count('hits', filter=Q(articlehit__created__gt=last_month))).order_by('-count', '-publish_Article')[:5],
         "title" : "مقالات پر بازدید ماه"
    }


@register.inclusion_tag("registration/partials/sidebar.html")
def hot_articles(): # توی فایل .html   ازش استفاده کرده ام
    last_month = datetime.today() - timedelta(days=30)
    # content_type_id = user_type = ContentType.objects.get(app_label='Articles', model='ArticlesModel').id
    return {
        # دسته بندی ها
         "articles" : ArticlesModel.objects.published().order_by('-publish_Article').annotate(count=Count('comments', filter=Q(comments__posted__gt=last_month) and Q(comments__content_type_id=13))).order_by('-count', '-publish_Article')[:5],
        #  "articles" : ArticlesModel.objects.published().order_by('-publish_Article').annotate(count=Count('comments', filter=Q(comments__posted__gt=last_month) and Q(comments__content_type_id=content_type_id))).order_by('-count', '-publish_Article')[:5],
         "title" : "مقالات داغ ما"
    }
