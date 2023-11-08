from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , CreateView , UpdateView
from Articles.models import ArticlesModel
from .mixins import fieldsMixin , FormValidMixin , AuthorAccessMixin


# @login_required
# def home_account(request):
#     return render(request, "registration/home_account.html")


# مربوط به نمایش مقالات به ازای هر نویسنده
class ArticleListAccount(LoginRequiredMixin,ListView):
    # queryset = ArticlesModel.objects.all().order_by('-publish_Article')
    template_name = "registration/home_account.html"
    # paginate_by = 2
    def get_queryset(self):
        if self.request.user.is_superuser:
            return ArticlesModel.objects.all().order_by('-publish_Article')
        else:
            return ArticlesModel.objects.filter(author=self.request.user).order_by('-publish_Article')

class ArticleCreateViewAccount(LoginRequiredMixin , FormValidMixin , fieldsMixin , CreateView):
    model = ArticlesModel
    # fields = [ 'author' , 'image_Article' , 'File_Article' , 'title_Article' , 'slug_Article', 'Abstract_Article', 'Key_word_Article', 'Introduction_Article', 'Body_or_text_Article', 'Result_Article', 'References_Article', 'category_Article', 'Article_type_Article', 'is_sale_Article' , 'status_Article' ]
    template_name = "registration/article_create_update.html"

class ArticleUpdateViewAccount(AuthorAccessMixin , FormValidMixin , fieldsMixin , UpdateView):
    model = ArticlesModel
    template_name = "registration/article_create_update.html"
