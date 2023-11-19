from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from Articles.models import ArticlesModel
from .mixins import fieldsMixin , FormValidMixin , AuthorAccessMixin , superuserAccessMixin , AthorsAccessMixin
from django.urls import reverse_lazy
from .models import User
from .forms import ProfileForm
from django.contrib.auth.views import LoginView , PasswordChangeView



# @login_required
# def home_account(request):
#     return render(request, "registration/home_account.html")


# مربوط به نمایش مقالات به ازای هر نویسنده
class ArticleListAccount(AthorsAccessMixin,ListView):
# class ArticleListAccount(LoginRequiredMixin,ListView):
    # queryset = ArticlesModel.objects.all().order_by('-publish_Article')
    template_name = "registration/home_account.html"
    # paginate_by = 2
    def get_queryset(self):
        if self.request.user.is_superuser:
            return ArticlesModel.objects.all().order_by('-publish_Article')
        else:
            return ArticlesModel.objects.filter(author=self.request.user).order_by('-publish_Article')

class ArticleCreateViewAccount(AthorsAccessMixin , FormValidMixin , fieldsMixin , CreateView):
# class ArticleCreateViewAccount(LoginRequiredMixin , FormValidMixin , fieldsMixin , CreateView):
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


# class PasswordChange(PasswordChangeView):
#     success_url = reverse_lazy("ACCOUNT:password_change_done")



















from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_text
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
# from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def _camelize_django_str(s):
    if isinstance(s, Promise):
        s = force_str(s)
    return to_camel_case(s) if isinstance(s, six.string_types) else s

class register(CreateView):
    form_class = SignupForm
    template_name = "registration/register.html"

    def form_valid(self ,form):
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(self.request)
            mail_subject = 'فعال سازی اکانت '
            message = render_to_string('registration/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('لینک فعالسازی به ایمیل شما ارسال شد .  <a href="/login" > ورود </a>')




# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your blog account.'
#             message = render_to_string('acc_active_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token':account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(
#                         mail_subject, message, to=[to_email]
#             )
#             email.send()
#             return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})





def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        return HttpResponse('با تشکر از شما برای تایید ایمیل شما. اکنون می توانید به حساب کاربری خود وارد شوید. <a href="/login" > ورود </a>')
    else:
        return HttpResponse('لینک فعال سازی نامعتبر است! <a href="/register" > ورود </a>')