from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView, DeleteView
from Blog_App.models import BlogModel, CommentModel, LikeModel
from Blog_App.forms import CommentForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

# Create your views here.

# def blog_list(request):
#     blogs = BlogModel.objects.all()

#     return render(request, 'Blog_App/blog_list.html', context={'blogs':blogs})


class CreateblogView(LoginRequiredMixin, CreateView):
    model = BlogModel
    template_name = "Blog_App/create_blog.html"
    fields = ('blog_title', 'blog_content', 'blog_image',)

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

class BlogList(ListView):
    context_object_name = "blogs"
    model = BlogModel
    template_name = 'Blog_App/blog_list.html'
    #queryset = BlogModel.objects.order_by('-publish_date')

@login_required
def blog_details(request, slug):
    blog = BlogModel.objects.get(slug=slug)
    comment_form = CommentForm()
    already_liked = LikeModel.objects.filter(blog=blog, user= request.user)

    if already_liked:
        liked = True
    else:
        liked = False
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit = False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            
            return HttpResponseRedirect(reverse('Blog_App:blog_details', kwargs={'slug':slug}))

    return render(request, 'Blog_App/blog_details.html', context={'blog' : blog, 'comment_form' : comment_form, 'liked' : liked})



@login_required
def liked(request, pk):
    blog = BlogModel.objects.get(pk = pk)
    user = request.user
    already_liked = LikeModel.objects.filter(blog=blog, user=user)

    if not already_liked:
        liked_post = LikeModel(blog=blog, user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('Blog_App:blog_details', kwargs={'slug':blog.slug}))

@login_required
def unliked(request, pk):
    blog = BlogModel.objects.get(pk=pk)
    user = request.user
    already_liked = LikeModel.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('Blog_App:blog_details', kwargs={'slug':blog.slug}))
    if already_liked:
        unliked_post = LikeModel.objects.get(blog)