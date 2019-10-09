from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm
# Create your views here.

def blog_publish(request):
    posts = Blog.objects.order_by('-created','created')
    return render(request, 'blogpublish/list_publish.html',{'posts':posts})

def blog_detail(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    try:
        selected_post = Blog.objects.get(pk=blog_id)
    except (KeyError, Blog.DoesNotExists):
        return render(request, 'blogpublish/detail_publish.html',{'post':post,'error_message': "No existe esta publicacion",})
    else:
        return render(request, 'blogpublish/detail_publish.html',{'post':post})

@login_required
def create(request):
    if request.method == 'POST':
        blogForm = BlogForm(request.POST , request.FILES)

        if blogForm.is_valid():
            blog_form = blogForm.save(commit=False)
            blog_form.author = request.user
            blog_form.save()

            return redirect(reverse('publish-posts'))
        else:
            print(blogForm.errors)
    else:
        blogForm = BlogForm()
    return render(request,'blogpublish/create_publish.html',{'blogForm':blogForm})

@login_required
def blog_update(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    blogForm = BlogForm(request.POST or None, request.FILES or None, instance=post)

    if request.POST and blogForm.is_valid():
        blogForm.save()

        return redirect(reverse('detail-publish', args=[blog_id]))
    
    return render(request, 'blogpublish/update_publish.html',{'blogForm':blogForm})

@login_required
def blog_delete(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        post.delete()
        return redirect(reverse('publish-posts'))
    
    return render(request, 'blogpublish/delete_publish.html',{'post':post})
