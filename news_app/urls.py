from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('info/', views.info, name='info'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-article/', views.add_article, name='add_article'),
]