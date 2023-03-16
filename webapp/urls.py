from django.contrib import admin
from django.urls import path

from .views.articles import ArticleCreateView, ArticleDetail,ArticleUpdateView,ArticleDeleteView
from .views.base import IndexView
from .views.project_functions import ProjectDetail, ProjectCreateView
from .views.projects import ProjectView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles/add/', ArticleCreateView.as_view(), name='article_add'),
    path('articles/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('articles/<int:pk>/confirm-delete/', ArticleDeleteView.as_view(), name='confirm_delete'),
    path('articles/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('projects/', ProjectView.as_view(), name='projects'),
    path('projects/<int:pk>', ProjectDetail.as_view(), name='project_detail'),
    path('projects/add/', ProjectCreateView.as_view(), name='project_add')
]