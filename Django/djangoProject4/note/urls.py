# -*- coding: UTF-8 -*-
from django.urls import path
from . import views
urlpatterns=[
    path('all',views.list_view),
    path('add',views.add_view)
]