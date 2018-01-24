from django.shortcuts import render

# Create your views here.
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

@csrf_exempt
def register(request):
    errors = []
    username = None
    password = None
    password2 = None
    email = None
    CompareFlag = False
    if request.method == 'POST':
        if not request.POST.get('username'):
            errors.append('账号不能为空')
        else:
            username = request.POST.get('username')
            try:
                exist = User.objects.get(username=username)
                username = None
                errors.append("该用户名已被使用")
            except:
                pass
        if not request.POST.get('password'):
            errors.append('密码不能为空')
        else:
            password = request.POST.get('password')
        if not request.POST.get('password2'):
            errors.append('确认密码不能为空')
        else:
            password2 = request.POST.get('password2')
        if not request.POST.get('email'):
            errors.append('邮箱不能为空')
        else:
            email = request.POST.get('email')
            try:
                exist = User.objects.get(email=email)
                email = None
                errors.append("该邮箱已被使用")
            except:
                pass
        if password:
            if password == password2:
                CompareFlag = True
            else:
                errors.append("两次输入的密码不一致")

        #无任何问题创建
        if not errors:
            user = User.objects.create_user(username, email, password)
            user.save()
            #自动跳转登录
            userlogin = auth.authenticate(username=username, password=password)
            auth.login(request,userlogin)
            return HttpResponseRedirect('/')
    return render(request, 'register.html',{'errors': errors})
#登录
def login(request):
    errors = []
    username = None
    password = None

    if request.method == 'POST':
        if not request.POST.get('username'):
            errors.append('账号不能为空')
        else:
            username = request.POST.get('username')
        if not request.POST.get('password'):
            errors.append('密码不能为空')
        else:
            password = request.POST.get('password')
        if username and password:
            print(username,password)
            user = auth.authenticate(username=username,password=password)
            print(user)
            if user:
                if user.is_active:
                    auth.login(request,user)
                    return HttpResponseRedirect('/')
                else:
                    errors.append("用户名错误")
            else:
                errors.append("用户名或密码错误")

    return render(request, 'login.html',{'errors':errors})

#用户登出
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")