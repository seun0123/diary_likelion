from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from django.utils import timezone
from .models import Blog

# Create your views here.
def index(request):
    return render(request, 'main.html')

def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form = form.save(commmit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('main')
    else:
        form = BlogForm
        return render(request, 'write.html', {'form' : form})

def read(request):
    blogs = Blog.object
    return render(request, 'read.html', {'blogs':blogs})

def read(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'read.html', {'blog':blog})