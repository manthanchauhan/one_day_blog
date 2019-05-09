from django.contrib import admin
from django.urls import path
from articles import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login_page/', auth_views.LoginView.as_view(), name='login_url'),
    path('logout_page/', auth_views.LogoutView.as_view(), name='logout_url'),
    path('', views.home, name='home_url'),
    path('admin/', admin.site.urls, name='admin_url'),
    path('articles/<int:id_>/', views.article, name='article_url'),
    path('tags/<int:id_>/', views.tag, name='tag_url'),
    path('signup_page/', accounts_views.signup, name='signup_url'),
    path('articles_page/', views.articles, name='articles_url'),
    path('tags_page/', views.tags, name='tags_url'),
    path('admin_profile_page/', views.admin_profile, name='admin_profile_url')
]
