from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.
def post_list(request):
    post = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    return render(request,'post.html',{'post':post})
    # return render(request,'index.html')