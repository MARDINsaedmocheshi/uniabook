from django import template
from ..models import Category , ArticlesModel
from django.db.models import Count , Q
from datetime import datetime , timedelta


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




@register.inclusion_tag("registration/partials/popular_articles.html")
def popular_articles(): # توی فایل popular_articles.html   ازش استفاده کرده ام
    last_month = datetime.today() - timedelta(days=30)
    return {
        # دسته بندی ها
         "popular_articles" : ArticlesModel.objects.published().order_by('-publish_Article').annotate(count=Count('hits', filter=Q(articlehit__created__gt=last_month))).order_by('-count', '-publish_Article')[:5]

    }
