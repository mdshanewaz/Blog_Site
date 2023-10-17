from django.contrib import admin
from Blog_App.models import BlogModel, LikeModel, CommentModel

# Register your models here.

admin.site.register(BlogModel)
admin.site.register(CommentModel)
admin.site.register(LikeModel)