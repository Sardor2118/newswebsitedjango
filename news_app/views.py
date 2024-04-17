from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Article, Category, Search
from .forms import ArticleForm


def home(request):
    articles = Article.objects.all().order_by('-published_at')
    context = {'articles': articles}
    return render(request, 'news_app/home.html', context)


def info(request):
    return render(request, 'news_app/info.html')


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'news_app/article_detail.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'news_app/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'news_app/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'news_app/add_article.html', context)
