# urls.py
from django.urls import path
from .views import (
    PostListView, PostDetailView, blog_by_category, blog_by_tag, add_comment, search_posts
)
from . import views

urlpatterns = [
    # Home/Blog List View
    path('', PostListView.as_view(), name='blog'),

    # Post Detail View
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Filter Posts by Category
    path('category/<int:category_id>/', blog_by_category, name='blog-by-category'),

    # Filter Posts by Tag
    path('tag/<int:tag_id>/', blog_by_tag, name='blog-by-tag'),

    # Add Comment
    path('post/<int:post_id>/comment/', add_comment, name='add-comment'),

    path('search/', search_posts, name='blog-search'),  # Add this line
]
