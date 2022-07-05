from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

def index(request):
    # 获取浏览器的ip地址
    user_ip = request.META['REMOTE_ADDR']
    print('user_ip is : '+user_ip)
    return render(request, 'news/index.html')

def login(request):
    '''用户登录'''
    if request.method == 'GET':
        '''显示注册页面'''
        return render(request, 'news/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        times = request.POST.get('times')
        print('提交时间为: '+times)
        if username == 'pk' and password =='123':
            return render(request,'news/index.html')



#news/set_cookie
def set_cookie(request):
    '''测试浏览器保存cookie'''
    response = HttpResponse('设置cookie')
    response.set_cookie('num',1,max_age=24*3600*7)
    return response

def get_cookie(request):
    '''测试获取cookie'''
    num = request.COOKIES['num']
    return HttpResponse(num)