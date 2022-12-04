from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import View

class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 判断是否为空
        # 进行业务处理：登录处理
        user = authenticate(request,username=username,password=password)
        if user is None:
            return render(request,'login.html',{'errmsg':'用户名或密码错误'})
        login(request, user)
        next_url = request.GET.get('next', reverse('dcim:index'))

        # 跳转到next_url
        response = redirect(next_url)
        return response


class LogoutView(View):
    def get(self,request):
        logout(request)
        # 跳转到首页
        return redirect(reverse('user:login'))
