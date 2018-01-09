from django.shortcuts import render

# Create your views here.
#首页
def index(request):
    return render(request,"index.html")
#创建帖子页面
def create_post(request):
    return render(request,'create_post.html')