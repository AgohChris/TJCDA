from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

# Helper pour vérifier si l'utilisateur est staff
def is_staff(user):
    return user.is_staff

# ===========================================
# ROUTES PUBLIQUES
# ===========================================

def index(request):
    """Page d'accueil"""
    return render(request, 'pages/index.html')

def about(request):
    """Page À propos"""
    return render(request, 'pages/about.html')

def authors_list(request):
    """Liste des auteurs/contributeurs"""
    return render(request, 'pages/authors.html')

def articles_list(request):
    """Catalogue des articles"""
    return render(request, 'pages/articles.html')

def article_detail(request, slug=None):
    """Détail d'un article"""
    # Pour l'instant, on affiche le template statique
    # Plus tard, on récupérera l'article par son slug
    return render(request, 'pages/article_detail.html')

def login_view(request):
    """Page de connexion"""
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('gestion_dashboard')
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_staff:
                login(request, user)
                messages.success(request, 'Connexion réussie.')
                return redirect('gestion_dashboard')
            else:
                messages.error(request, 'Accès réservé aux administrateurs.')
        else:
            messages.error(request, 'Identifiants incorrects.')
    
    return render(request, 'pages/login.html')

def logout_view(request):
    """Déconnexion"""
    logout(request)
    messages.info(request, 'Vous avez été déconnecté.')
    return redirect('index')

# ===========================================
# ROUTES GESTION (Dashboard Admin)
# ===========================================

@login_required(login_url='login')
@user_passes_test(is_staff, login_url='login')
def gestion_dashboard(request):
    """Tableau de bord de gestion"""
    return render(request, 'gestion/dashboard.html')

@login_required(login_url='login')
@user_passes_test(is_staff, login_url='login')
def gestion_articles(request):
    """Liste des articles"""
    return render(request, 'gestion/articles.html')

@login_required(login_url='login')
@user_passes_test(is_staff, login_url='login')
def gestion_article_create(request):
    """Création d'article"""
    return render(request, 'gestion/article_edit.html', {'is_edit': False})

@login_required(login_url='login')
@user_passes_test(is_staff, login_url='login')
def gestion_article_edit(request, article_id):
    """Édition d'article"""
    return render(request, 'gestion/article_edit.html', {'is_edit': True, 'article': {'id': article_id}})

@login_required(login_url='login')
@user_passes_test(is_staff, login_url='login')
def gestion_categories(request):
    """Gestion des catégories"""
    return render(request, 'gestion/categories.html')

@login_required(login_url='login')
@user_passes_test(is_staff, login_url='login')
def gestion_auteurs(request):
    """Gestion des auteurs"""
    return render(request, 'gestion/auteurs.html')
