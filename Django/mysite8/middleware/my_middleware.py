# -*- coding: UTF-8 -*-
import re
import traceback

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.core import mail
from django.conf import settings

class MyMW(MiddlewareMixin):

    def process_request(self, request):
        print('MyMW process_request do --')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('MyMW process_view do --')

    def process_response(self, request, response):
        print('MyMW process_response do --')
        return response


class MyMW2(MiddlewareMixin):

    def process_request(self, request):
        print('MyMW2 process_request do --')


    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('MyMW2 process_view do --')


    def process_response(self, request, response):
        print('MyMW2 process_response do --')
        return response


# 访问过多限制器（中间件）
class VisitLimit(MiddlewareMixin):
    visit_times = {}

    def process_request(self, request):
        ip_address = request.META['REMOTE_ADDR']  # 获取IP的固定用法
        path_url = request.path_info  # 获取路径
        if not re.match('^/test', path_url):
            return
        times = self.visit_times.get(ip_address, 0)
        print('ip', ip_address, '已经访问', times)
        self.visit_times[ip_address] = times + 1
        if times < 5:
            return
        return HttpResponse('您已经访问过' + str(times) + '次，访问被禁止')


#  网站报错，发送邮件
class ExceptionMW(MiddlewareMixin):
    def process_exception(self, request, exception):
        print(exception)
        print(traceback.format_exc())  # 详细报错
        mail.send_mail(subject='报错',message='traceback.format_exc()',
                       from_email='519793331@qq.com',recipient_list=settings.EX_EMAIL)
        return HttpResponse('当前网站异常')