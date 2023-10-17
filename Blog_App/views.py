from django.shortcuts import render

# Create your views here.

def blog_list(request):
    return render(request, 'Blog_App/blog_list.html', context={})