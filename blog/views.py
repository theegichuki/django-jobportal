from django.shortcuts import render

# Create your views here.
def blog_page(request):
    return render(request, 'blog/blog.html')

def blog_details(request):
    return render(request, 'blog/blog-details.html')
