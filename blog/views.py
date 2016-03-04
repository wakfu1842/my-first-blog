from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
"""from 後面的點號意味著 當前目錄 或 當前的應用程序。 因為 views.py 和 models.py 是在同一目錄中，我們只需要使用 . 和 文件的名稱（無 .py) 。 然後我們導入模型（Post)"""

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})