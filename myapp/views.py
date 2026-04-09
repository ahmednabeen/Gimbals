from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post
from .forms import ContactForm

def index(request):
    # Fetch the 9 most recent posts to display on the home page
    latest_posts = Post.objects.all()[:9]
    context = {
        'posts': latest_posts
    }
    return render(request, 'index.html', context)

def blog(request):
    # Fetch all post objects to display on the blog page
    all_posts = Post.objects.all()
    context = {
        'posts': all_posts
    }
    return render(request, 'blog.html', context)

def blog_detail(request, slug):
    # Fetch the specific post using its slug, or return a 404 error if not found
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'blog_detail.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # If the form has been submitted, process the data
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # Save the new contact message to the database
            messages.success(request, 'Your message has been sent successfully! We will get back to you shortly.')
            return redirect('contact')
    else:
        # If it's a GET request, just display a new, blank form
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

def privacy(request):
    return render(request, 'privacy.html')

def disclaimer(request):
    return render(request, 'disclaimer.html')
