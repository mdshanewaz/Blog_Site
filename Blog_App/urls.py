from django.urls import path
from . import views
# from Blog_App import views

app_name = 'Blog_App'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateblogView.as_view(), name='create_blog'),
    
]