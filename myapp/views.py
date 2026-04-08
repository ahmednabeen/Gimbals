from django.shortcuts import render, redirect
from .models import Post 
from .forms import ContactForm
from django.contrib import messages

# ... your index view ...
def index(request):
    latest_posts = Post.objects.all()[:9]
    context = {
        'posts': latest_posts
    }
    return render(request, 'index.html', context)


def blog(request):
    # Fetch all post objects from the database
    all_posts = Post.objects.all()
    
    # Create the context dictionary
    context = {
        'posts': all_posts
    }
    
    # Pass the context to the blog.html template
    return render(request, 'blog.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        # If the form has been submitted, process the data
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # Save the new contact message to the database
            
            # Add a success message
            messages.success(request, 'Your message has been sent successfully! We will get back to you shortly.')
            
            # Redirect to the same contact page (or a 'thank you' page)
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
