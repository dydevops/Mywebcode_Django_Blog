from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Post,BlogComment,Category
from django.contrib import messages
from blog.templatetags import extras
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.
# def home(request):
#     return HttpResponse("<h1>This is Home Page Website</h1>")

# def post(request):
#     return HttpResponse("<h1>This is Blog  Page Website</h1>")


def bolgHome(request,category_slug=None):
    categories = None
    allPosts = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        recent_posts = Post.objects.filter(status=1)[0:5]
        allPosts = Post.objects.filter(category=categories, status=1)
        paginator = Paginator(allPosts, 5)
        page = request.GET.get('page')
        paged_posts = paginator.get_page(page)
        # post_count = allPosts.count()
    else:
        # allPosts = Post.objects.filter(status=1).order_by('-created_on')
        recent_posts = Post.objects.filter(status=1)[0:5]
        allPosts = Post.objects.all().filter(status=1).order_by('created_on')
        paginator = Paginator(allPosts, 5)
        page = request.GET.get('page')
        paged_posts = paginator.get_page(page)
    context ={
        'allPosts': paged_posts,
        'recent_posts':recent_posts,
        # 'post_count':post_count,
    }
    return render(request, 'blog/blog-list.html',context)

def blogPost(request, post_slug):
    # single_post = get_object_or_404(Post, slug=post_slug)
    recent_posts = Post.objects.filter(status=1)[0:5]
    post = Post.objects.filter(slug=post_slug).first()
    post.save()
    
    comments = BlogComment.objects.filter(post=post, parent=None).order_by('-created_on')
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
            
            
    context ={
            'post': post,
            'recent_posts':recent_posts,
            'comments':comments,
            'user':request.user, 
            'replyDict':replyDict,
        }
    
    return render(request, 'blog/blog-details.html',context)


def search(request):
    if 'keyword' in request.GET:
        query = request.GET['keyword']
        if query:
            allPosts = Post.objects.order_by('-created_on').filter(Q(content__icontains=query) | Q(title__icontains=query))
            recent_posts = Post.objects.filter(status=1)[0:2]
        else: 
           allPosts = Post.objects.filter(status=1).order_by('-created_on')[0:4]  
           recent_posts = Post.objects.filter(status=1)[0:3]  
    context = {
        'allPosts': allPosts,
        'query':query, 
        'recent_posts':recent_posts, 
    }
    return render(request, 'blog/blog-list.html', context)


def postComment(request):
    if request.method=="POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
    
        
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
    return redirect(f"/blog/{post.slug}")

