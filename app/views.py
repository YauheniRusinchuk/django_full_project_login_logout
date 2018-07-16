from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST ,require_http_methods
from django.urls import reverse
from .models import Post,Comment
from .forms import PostForm, FormComments
from django.db.models import Q

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'app/index.html', {"posts": posts})


def about(request):
    return render(request, 'app/about.html', {})


@require_http_methods(['GET', 'POST'])
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    form = FormComments()
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    if request.method == 'POST':
         com = request.POST.get('comment')
         print('comment :', com)
         new_comment = Comment(text=com, post=post)
         new_comment.save()
         return HttpResponseRedirect('/postnumber/{}'.format(pk))
    return render(request, 'app/detail.html', context)





@require_POST
def search(request):
    if request.method == "POST":
        srch = request.POST['search_text']
        if srch:
            match = Post.objects.filter(Q(content__icontains=srch)|
                                        Q(content__contains=srch))
            if match:
                return render(request, 'app/search.html', {'result':match})

            else:
                return render(request, 'app/search.html', {})


def profile(request, fullname):
    user = User.objects.get(last_name=fullname)
    posts = Post.objects.filter(user=user)
    description = user.user_profile.description
    avatar = user.user_profile.avatar.url
    name = user.first_name + " " + user.last_name
    context = {
        'name' : name,
        'description' : description,
        'avatar' : avatar,
        'posts' : posts,
    }
    return render(request, 'app/profile.html', context)
    #return redirect('index')


@require_POST
def addpost(request):
    if request.method == "POST":
        print("before form")
        postform = PostForm(request.POST,request.FILES)
        print('after form')
        if postform.is_valid():
            print("IS VALID")
            post = Post(user=request.user,img = request.FILES['imgfile'], content=request.POST['content'])
            post.save()
            print("POST SAVE")
            return redirect('index')


def add_post(request):
    if request.user.is_authenticated:
        form = PostForm()
        return render(request, 'app/add_post.html', {'form': form})
    return HttpResponseRedirect("/")

