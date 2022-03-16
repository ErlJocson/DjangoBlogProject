from .views import *
from django.urls import path

urlpatterns = [
    path('', index_view, name='home'),
    path('blog-comment/<int:blog_id>', blog_comment_view, name='comments-likes'),
    path('like/<int:blog_id>', like_post, name="like_post")
]