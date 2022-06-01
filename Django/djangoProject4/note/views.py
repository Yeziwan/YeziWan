from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Note
# Create your views here.
def check_login(fn):
    def wrap(request,*args,**kwargs):
        #检查session
        if 'username' not in request.session or 'uid' not in request.session:
            #检查COOKIES
            c_username=request.COOKIES.get('username')
            c_uid=request.COOKIES.get('uid')
            if not c_username or not c_uid:
                return HttpResponseRedirect('user/login')
            else:
                #回写session
                request.session['username']=c_username
                request.session['uid']=c_uid
            return fn(request,*args,**kwargs)
    return wrap


def list_view(request):
    all_note=Note.objects.all()
    return render(request,'note/list_note.html',locals())


def add_view(request):
    if request.method=="GET":
        return render(request,'note/add_note.html')
    elif request.method=="POST":
        uid=request.session['uid']
        title=request.POST['title']
        content=request.POST['content']
        Note.objects.create(title=title,content=content,user_id=uid)
        return HttpResponse('笔记添加成功')
