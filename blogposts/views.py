from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, Comment

# Create your views here.
def home(request):
    Blog_Posts = BlogPost.objects.order_by('-pub_date')
    return render(request, 'blogposts/home.html', {'BlogPosts': Blog_Posts})

def post_details(request, post_id):
    #blog_post = BlogPost.objects.get(pk=post_id)
    if request.method == "POST":
        username = request.POST['username']
        message = request.POST['comment']
        post_id = request.POST['post_id']
        comment = Comment.create(username, message, post_id)
        comment.save()
        Blog_Post = get_object_or_404(BlogPost, pk=post_id)
        #comments = Comment.objects.get(post_id=post_id)
        comments = Comment.objects.filter(post_id=post_id)
        return redirect('posts_detail', post_id=post_id)
    else:
        Blog_Post = get_object_or_404(BlogPost, pk=post_id)
        comments = Comment.objects.filter(post_id=post_id)
        return render(request, 'blogposts/posts_detail.html', {'BlogPost':Blog_Post, 'Comments': comments })
