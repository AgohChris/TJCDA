from django.shortcuts import render

# --- Public Views ---

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    """Page À propos"""
    return render(request, 'pages/about.html')

def authors_list(request):
    """Liste des auteurs (si le template existait)"""
    # Placeholder si on réactive authors.html plus tard
    return render(request, 'pages/authors.html')

def articles_list(request):
    """Catalogue des articles"""
    return render(request, 'pages/articles.html')

def article_detail(request):
    """Détail d'un article (statique pour l'instant)"""
    return render(request, 'pages/article_detail.html')

def login_view(request):
    """Page de connexion"""
    return render(request, 'pages/login.html')


# --- Admin Views ---

def admin_dashboard(request):
    """Tableau de bord Admin"""
    return render(request, 'pages/admin_dashboard.html')

def admin_articles(request):
    """Backend : Liste des articles"""
    return render(request, 'pages/admin_articles.html')

def admin_article_create(request):
    """Backend : Création d'article"""
    return render(request, 'pages/admin_article_edit.html', {'is_edit': False})

def admin_article_edit(request, article_id):
    """Backend : Édition d'article"""
    return render(request, 'pages/admin_article_edit.html', {'is_edit': True, 'article': {'id': article_id}})
