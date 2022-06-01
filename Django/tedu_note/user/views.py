import hashlib

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
# Create your views here.


def reg_view(request):
    """
    注册界面
    """
    if request.method == 'GET':
        # GET返回页面
        return render(request, 'user/register.html')

    # POST处理提交数据
    elif request.method == "POST":
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']

        # 1、两个密码要保持一直
        if password_1 != password_2:
            return HttpResponse('密码不一致，请重新输入')
        else:
            h = hashlib.md5()
            h.update(password_1.encode())  # encode()将普通的字符串密码转换成字节串
            password = h.hexdigest()

        # 2、校验当前用户名是否可用
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('用户名不可用')

        # 3、插入数据
        try:  # 使用try，防止并发
            user = User.objects.create(username=username, password=password)
        except Exception as e:
            print('--create user error %s' % e)
            return HttpResponse('用户名不可用')

        #  设置免登录一天
        request.session['username'] = username
        request.session['uid'] = user.id  # 主键查询会比关键词查询更快

        #  修改session的存储时间一天
        #  该配置位于setting中 SESSION_COOKIE_AGE = 86400

        return HttpResponseRedirect('/index')


def login_view(request):
    """
    登录界面
    """
    if request.method == 'GET':
        # 跳转登录界面
        if request.session.get('username') and request.session.get('uid'):
            return render(request, 'index.html')
        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            return render(request, 'index.html')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        input_username = request.POST['username']
        input_password = request.POST['password']
        try:
            user = User.objects.get(username=input_username)
        except Exception as e:
            print('--login error as %s' % e)
            return HttpResponse('账号或密码错误，请重新输入')
        m = hashlib.md5()
        m.update(input_password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('账号或密码错误，请重新输入')
        else:
            request.session['username'] = input_username
            request.session['uid'] = user.id
            resp = HttpResponseRedirect('/index')
        if 'remember' in request.POST:
            resp.set_cookie('username', input_password, 3600*24*3)
            resp.set_cookie('uid', user.id, 3600*24*3)
        return resp


def logout_view(request):
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']
    resp = HttpResponseRedirect('/index')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp