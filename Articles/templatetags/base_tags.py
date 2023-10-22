from django import template

register = template.Library()

@register.simple_tag
def Title(data= "دانشگاه کتاب و مقاله"):     # این یک مقدار پیش فرض یا دیفالت است که اگر چیزی ننویسیم همین را برمیگرداند 
    return data
