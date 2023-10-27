from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    blog_title = models.CharField(max_length=300, verbose_name="Put a Title")
    slug = models.SlugField(max_length=100, unique=True)
    blog_content = models.TextField(verbose_name="What is on your mide?")
    blog_image = models.ImageField(upload_to="blog_img", verbose_name="Image")
    publis_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title 


class CommentModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name="blog_comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    comment = models.TextField(max_length=500)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class LikeModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name="liked_blog")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likers")
    
    def __str__(self):
        return self.user + "likes" + self.blog