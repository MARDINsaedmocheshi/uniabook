from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from Articles.models import ArticlesModel
from .mixins import fieldsMixin , FormValidMixin , AuthorAccessMixin , superuserAccessMixin
from django.urls import reverse_lazy
from .models import User
from .forms import ProfileForm
from django.contrib.auth.views import LoginView




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

class ArticleDeleteViewAccount(superuserAccessMixin , DeleteView):
    model = ArticlesModel
    success_url = reverse_lazy("ACCOUNT:home_account")
    template_name = "registration/articlesmodel_confirm_delete.html"


class Profile(LoginRequiredMixin , UpdateView):
    model = User
    template_name = "registration/profile.html"
    # fields = ['username','email','first_name','last_name','special_user','is_author']
    form_class = ProfileForm
    success_url = reverse_lazy("ACCOUNT:profile")

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk )
# در اینجا داریم یوزر رو میفرستیم به فرم برای اینکه سوپر یوزر ها بتونن نام و سایر فیلدهای خود را عوض کنند در پنل کاتربری که ساختیم
    def get_form_kwargs(self):
        kwargs = super(Profile , self).get_form_kwargs()
        kwargs.update ({
            'user' : self.request.user
        })
        return kwargs

class Login(LoginView):
    def get_success_url(self):
        user = self.request.user

        if user.is_superuser or user.is_author:
            return reverse_lazy("ACCOUNT:home_account")
        else:
            return reverse_lazy("ACCOUNT:profile")
