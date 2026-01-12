from django.urls import path
from . import views

urlpatterns = [
    # Routes Publiques
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('authors/', views.authors_list, name='authors_list'),
    path('articles/', views.articles_list, name='articles_list'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Routes Gestion (Dashboard Admin personnalisé)
    path('gestion/', views.gestion_dashboard, name='gestion_dashboard'),
    path('gestion/articles/', views.gestion_articles, name='gestion_articles'),
    path('gestion/articles/nouveau/', views.gestion_article_create, name='gestion_article_create'),
    path('gestion/articles/modifier/<int:article_id>/', views.gestion_article_edit, name='gestion_article_edit'),
    path('gestion/categories/', views.gestion_categories, name='gestion_categories'),
    path('gestion/auteurs/', views.gestion_auteurs, name='gestion_auteurs'),
]
