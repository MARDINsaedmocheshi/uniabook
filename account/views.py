from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from Articles.models import ArticlesModel

# @login_required
# def home_account(request):
#     return render(request, "registration/home_account.html")



class ArticleListAccount(LoginRequiredMixin,ListView):
    # queryset = ArticlesModel.objects.all().order_by('-publish_Article')
    template_name = "registration/home_account.html"
    # paginate_by = 2
    def get_queryset(self):
        if self.request.user.is_superuser:
            return ArticlesModel.objects.all().order_by('-publish_Article')
        else:
            return ArticlesModel.objects.filter(author=self.request.user).order_by('-publish_Article')

