from django.http import Http404
from django.shortcuts import  get_object_or_404
from Articles.models import ArticlesModel


class fieldsMixin():
    def dispatch(self , request , *args , **kwargs):
        if request.user.is_superuser:
            self.fields = [
                'author' , 'image_Article' , 'File_Article' , 'title_Article' ,'is_special', 'slug_Article', 'Abstract_Article', 'Key_word_Article', 'Introduction_Article', 'Body_or_text_Article', 'Result_Article', 'References_Article', 'category_Article', 'Article_type_Article', 'is_sale_Article' , 'status_Article'
                            ]
        elif request.user.is_author: #نویسندگان
            self.fields = [
                'image_Article' , 'File_Article' , 'title_Article' ,'is_special', 'slug_Article', 'Abstract_Article', 'Key_word_Article', 'Introduction_Article', 'Body_or_text_Article', 'Result_Article', 'References_Article', 'category_Article', 'Article_type_Article', 'is_sale_Article'
                            ]
        else:
            raise Http404("شما نمیتوانید این صفحه را ببینید")
        return super().dispatch(request , *args , **kwargs)

class FormValidMixin():
    def form_valid(self ,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author =  self.request.user
            self.obj.status_Article = 'd'
        return super().form_valid(form)                             







# دسترسی کاربران ادیت کردن مقاله
class AuthorAccessMixin():
    def dispatch(self , request ,pk , *args , **kwargs):
        article = get_object_or_404(ArticlesModel, pk=pk)

        if article.author == request.user and article.status_Article in ['j' , 'd'] or request.user.is_superuser:
            return super().dispatch(request , *args , **kwargs)      
        else:
            raise Http404("شما نمیتوانید این صفحه را ببینید")








# دسترسی کاربران حذف کردن مقاله
class superuserAccessMixin():
    def dispatch(self , request , *args , **kwargs):

        if request.user.is_superuser:
            return super().dispatch(request , *args , **kwargs)      
        else:
            raise Http404("شما نمیتوانید این صفحه را ببینید")
