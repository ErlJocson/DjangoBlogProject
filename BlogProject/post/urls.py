from .views import *
from django.urls import path

urlpatterns = [
    path('', index_view, name='home'),
    path('blog-comment/<int:blog_id>', blog_comment_view, name='comments-likes'),
    path('like/<int:blog_id>', like_post, name="like_post"),
    path('unlike/<int:blog_id>', unlike_post, name='unlike_post'),
    path('delete_blog/<int:blog_id>', delete_post, name='delete-post'),
    path('delete-comment/<int:blog_id>/<int:comment_id>', remove_comment, name='remove-comment')
]