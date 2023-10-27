from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView, DeleteView
from Blog_App.models import BlogModel, CommentModel, LikeModel
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

# Create your views here.

def blog_list(request):
    blogs = BlogModel.objects.all()

    return render(request, 'Blog_App/blog_list.html', context={"blogs": blogs})


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

