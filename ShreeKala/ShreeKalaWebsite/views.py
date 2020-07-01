from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'services.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def singleblog(request):
    return render(request, 'single-blog.html', {})

def contact(request):
    return render(request, 'contact.html', {})