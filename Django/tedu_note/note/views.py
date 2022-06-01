import csv

from upload.models import Content
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Note


# Create your views here.
def check_login(fn):
    """
    装饰器，验证当前网站登录状态
    """
    def wrap(request, *args, **kwargs):
        if 'username' not in request.session or 'uid' not in request.session:
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_username or not c_uid:
                return HttpResponseRedirect('user/login')
            else:
                request.session['username'] = c_username
                request.session['uid'] = c_uid
        return fn(request, *args, **kwargs)
    return wrap


# def list_view(request):
#     all_note = Note.objects.filter(is_active=True)
#     return render(request, 'note/list_note.html', locals())


@check_login
def add_view(request):
    """
    添加笔记
    """
    if request.method == "GET":
        return render(request, 'note/add_note.html')
    elif request.method == "POST":
        uid = request.session['uid']
        title = request.POST['title']
        content = request.POST['content']

        Note.objects.create(title=title, content=content, user_id=uid)
        return render(request, 'note/jump.html')


def updata_note(request, note_id):
    """
    更新笔记
    """
    try:
        note = Note.objects.get(id=note_id)
    except Exception as e:
        print('--updata note error is %s' % e)
        return HttpResponse('--The book is not existed')
    if request.method == "GET":
        return render(request, 'note/updata_note.html', locals())
    elif request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        note.title = title
        note.content = content
        note.save()
        return HttpResponseRedirect('/note/all')


def delete_note(request):
    """
    删除笔记
    """
    note_id = request.GET.get('note_id')
    if not note_id:
        return HttpResponse('---请求异常')
    try:
        note = Note.objects.get(id=note_id, is_active=True)
    except Exception as e:
        print('---delete note get error %s' % e)
        return HttpResponse('--get note.id is error')
    note.is_active = False
    note.save()
    return HttpResponseRedirect('/note/all')


def list_view(request):
    """
    制作页面页码
    """
    all_note = Note.objects.filter(is_active=True)
    note_list = []
    now_page_num = request.GET.get('page', 1)
    for note in all_note:
        dict = {}
        id = 1
        dict['title'] = note.title
        dict['content'] = note.content
        dict['created_time'] = note.created_time
        dict['updated_time'] = note.updated_time
        note_list.append(dict)
    paginator = Paginator(note_list, 10)
    now_page_content = paginator.page(int(now_page_num))
    return render(request, 'note/list_note.html', locals())


def make_page_csv(request):
    all_note = Note.objects.filter(is_active=True)
    note_list = []
    now_page_num = request.GET.get('page', 1)
    for note in all_note:
        dict = {}
        id = 1
        dict['title'] = note.title
        dict['content'] = note.content
        dict['created_time'] = note.created_time
        dict['updated_time'] = note.updated_time
        note_list.append(dict)
    paginator = Paginator(note_list, 10)
    now_page_content = paginator.page(int(now_page_num))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; ' \
                                      'filename="page-%s.csv"' % now_page_content

    writer = csv.writer(response)
    for page in now_page_content:
        writer.writerow([page])
    return response


def upload(request):
    if request.method == "GET":
        return render(request, 'note/upload.html')
    elif request.method == "POST":
        title = request.POST['title']
        myfile = request.FILES['myfile']
        Content.objects.create(title=title, picture=myfile)
        return render(request, 'note/jump.html')