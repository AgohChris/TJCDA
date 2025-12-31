from django.urls import path
from . import views

urlpatterns = [
    # Public Routes
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('authors/', views.authors_list, name='authors_list'), # Fixed: Added missing route
    path('articles/', views.articles_list, name='articles_list'),
    path('articles/detail/', views.article_detail, name='article_detail'),
    path('articles/detail/<int:article_id>/', views.article_detail, name='article_detail_dynamic'),
    path('login/', views.login_view, name='login'),

    # Admin Routes
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/articles/', views.admin_articles, name='admin_articles'),
    path('admin/articles/create/', views.admin_article_create, name='admin_article_create'),
    path('admin/articles/edit/<int:article_id>/', views.admin_article_edit, name='admin_article_edit'),
]
