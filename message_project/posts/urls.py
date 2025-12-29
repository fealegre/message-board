# posts/urls.py
from django.urls import path
from .views import (
    BlogCreateView, 
    BlogDeleteView, 
    BlogDetailView, 
    BlogUpdateView, 
    HomePageView
)

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(),name="post_delete"),
    path("", HomePageView.as_view(), name="home"),
]
