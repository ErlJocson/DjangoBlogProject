from .views import *
from django.urls import path

urlpatterns = [
    path('', index_view, name='home'),
    path('blog-comment/<int:blog_id>', blog_comment_view, name='comments-likes')
]