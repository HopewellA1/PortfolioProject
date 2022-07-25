from django.shortcuts import get_object_or_404, render
from .models import blog
from Blog.models import blog

# Create your views here.
def home(request):
    blogs = blog.objects.all()
    return render(request, 'Blog/home.html',{"Blogs": blogs})

def blogDetail(request,blog_id):
    blogd = get_object_or_404(blog,pk=blog_id)
    return render(request, 'Blog/blogDetail.html',{"blog":blogd})
    