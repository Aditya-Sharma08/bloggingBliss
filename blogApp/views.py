from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import UserCreationWithEmailForm
from django.contrib.auth.models import User

# Create your views here.

def helloWorld(request):
    return HttpResponse("Hello ji!")


def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)

    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(cat=cat, title__icontains=query)
    else:
        posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})

def about(request):
    return render(request, 'about.html')

def search_results(request):
    query = request.GET.get('q')
    posts = []
    if query:
        posts = Post.objects.filter(title__icontains=query)
    return render(request, 'category.html', {'posts': posts, 'query': query})

def register(request):
    if request.method == 'POST':
        form = UserCreationWithEmailForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_superuser(first_name=fname, last_name=lname, username=username, email=email, password=password)
            user.save() 
            return redirect('/admin/')  
    else:
        form = UserCreationWithEmailForm()
    return render(request, 'register.html', {'form': form}) 