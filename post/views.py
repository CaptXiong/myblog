from django.shortcuts import render
from .models import Post
import markdown
# from django.core.paginator import Paginator

def index(request):
    
    return render(request, 'post/index.html')

def blog(request):
    post = Post.objects.all()
    # limit = 3
    # paginator = Paginator(post, limit)
    # page = request.GET.get('page', 1)
    #
    # result = paginator.page(page)
    context = {
        "post_list":post
        # "post_list": result,
        # "page": page
    }
    return render(request, template_name='blog.html',context=context)

def detail(request,pk):
    post = Post.objects.get(id=pk)
    #post_list = Post.objects.all()
    # blog_all = Post.objects.all()
    post.body = markdown.markdown(post.body,
            extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
           ])
    context ={"post":post}
    return render(request, template_name='post/work.html', context=context)


