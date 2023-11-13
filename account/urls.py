from django.contrib.auth import views
from django.urls import path
from .views import ArticleListAccount , ArticleCreateViewAccount , ArticleUpdateViewAccount , ArticleDeleteViewAccount , Profile , Login


app_name = "ACCOUNT"
urlpatterns = [

    path("login/", Login.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),

    # path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    # path("password_change/done/",views.PasswordChangeDoneView.as_view(),name="password_change_done",),

    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path("password_reset/done/",views.PasswordResetDoneView.as_view(),name="password_reset_done",),

    # path("reset/<uidb64>/<token>/",views.PasswordResetConfirmView.as_view(),name="password_reset_confirm",),
    # path("reset/done/",views.PasswordResetCompleteView.as_view(), name="password_reset_complete",),

]


urlpatterns += [
    path("", ArticleListAccount.as_view() , name="home_account"),
    path("article/create", ArticleCreateViewAccount.as_view() , name="create_article"),
    path("article/update/<int:pk>", ArticleUpdateViewAccount.as_view() , name="update_article"),
    path("article/delete/<int:pk>", ArticleDeleteViewAccount.as_view() , name="delete_article"),
    path("profile/", Profile.as_view() , name="profile"),
]