from django import template
from ..models import Category


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
def link(request, link_name , content):
    return {
        # مربوط به اکتیو بودن منوها
         "request" : request,
         "link_name" : link_name ,
         "link" :  "ACCOUNT:{}".format(link_name),
         "content" : content,

    }