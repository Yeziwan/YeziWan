# -*- coding: UTF-8 -*-
import csv
import time

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(15)
def test_cache(request):
    t = time.time()
    return HttpResponse('t is %s' % t)


def test_mw(request):
    print('---test_mw view in ---')
    return HttpResponse('--test-mw--')


def test_page(request):
    page_num = request.GET.get('page', 1)  # 查询字符串获取页码test_page?page=1
    all_data = [i for i in range(1,11)]
    paginator = Paginator(all_data, 2)
    # 初始化具体页码的page对象，界面的内容
    c_page = paginator.page(int(page_num))
    return render(request, 'test_page.html', locals())


def test_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="test.csv"'
    all_data = [i for i in range(1,100)]
    writer = csv.writer(response)
    writer.writerow(all_data)
    return response


def make_page_csv(request):
    page_num = request.GET.get('page', 1)  # 查询字符串获取页码test_page?page=1
    all_data = [i for i in range(1,11)]
    paginator = Paginator(all_data, 2)
    # 初始化具体页码的page对象
    c_page = paginator.page(int(page_num))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; ' \
                                      'filename="page-%s.csv"' % page_num
    writer = csv.writer(response)
    for b in c_page:
        writer.writerow([b])
    return response