from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Blog(models.Model):
    content = models.TextField(max_length=256)
    date = models.DateTimeField(default=now, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Comment(models.Model):
    content = models.TextField(max_length=256)
    date = models.DateTimeField(default=now, editable=False)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Like(models.Model):
    is_like = models.BooleanField()
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.is_like