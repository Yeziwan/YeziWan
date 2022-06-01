# -*- coding: UTF-8 -*
import re
import traceback

from django.conf import settings
from django.core import mail
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class VisitLimit(MiddlewareMixin):
    """
    中间件：IP访问过多，禁止访问
    """
    visit_times = {}

    def process_request(self, request):
        ip_address = request.META['REMOTE_ADDR']
        path_url = request.path_info
        if not re.match('^/note', path_url):
            return
        times = self.visit_times.get(ip_address, 0)
        print('ip', ip_address, '已经访问', times)
        self.visit_times[ip_address] = times + 1
        if times < 100:
            return
        else:
            return HttpResponse('您已经访问过' + str(times) + '次，禁止访问')


class ExceptionMW(MiddlewareMixin):
    """
    出错报警，发送邮件
    """
    def process_exception(self, request, exception):
        mail.send_mail(subject='报错', message='traceback.format_exc()',
                       from_email='519793331@qq.com', recipient_list=settings)
        return HttpResponse('当前网络异常')