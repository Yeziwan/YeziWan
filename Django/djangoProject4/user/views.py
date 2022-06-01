from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
import hashlib
import time
# Create your views here.
def reg_view(request):
    if request.method=="GET":
        return render(request,'user/register.html')
    elif request.method=="POST":
        username=request.POST['username']
        password_1=request.POST['password_1']
        password_2 = request.POST['password_2']
        #1、确认密码是否一致
        if password_1 !=password_2:
            return HttpResponse("两次密码输入不一致")
        #加哈希算法
        m = hashlib.md5()
        m.update(password_1.encode())
        password_m=m.hexdigest()

        #2、确认用户名是否可用
        old_names=User.objects.filter(username=username)
        if old_names:
            return HttpResponse("用户名已注册")
        #3、插入数据
        try:#在此加try的意义是解决高并发
            user=User.objects.create(username=username,password=password_m)
        except Exception as e:
            print('---create user error%s'%(e))
            return HttpResponse('用户名已注册')
        #免登录一天
        request.session['username']=username
        request.session['uid']=user.id
        # return HttpResponse('注册成功,3秒后返回主页')
        # time.sleep(3)
        return HttpResponseRedirect('login')



def login_view(request):
    if request.method=="GET":
        #做免登录，先检查session，再检查cookie
        if request.session.get('username') and request.session.get('uid'):
            return HttpResponseRedirect('index')
        c_username=request.COOKIES.get('username')
        c_uid=request.COOKIES.get('uid')
        if c_username and c_uid:
            request.session['username']=c_username
            request.session['uid']=c_uid
            return HttpResponseRedirect('index')

        return render(request,'user/login.html')
    elif request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('---create user error%s'%(e))
            return HttpResponse('用户名或密码错误')
        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() !=user.password:
            return HttpResponse('用户名或密码错误')
        # 记录回话状态session
        request.session['username']=username
        request.session['uid']=user.id
        resp=HttpResponseRedirect('index')
        #判断用户是否点选了记住用户
        if 'remember' in request.POST:
            resp.set_cookie('username',username,3600*24*3)
            resp.set_cookie('uid',user.id, 3600 * 24 * 3)
        return resp

def index_view(request):
    return render(request,'user/index.html')

def logout(request):
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']
    resd=HttpResponseRedirect('login')
    if 'username' in request.COOKIES:
        resd.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resd.delete_cookie('uid')
    return resd
