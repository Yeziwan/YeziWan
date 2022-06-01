# -*- coding: UTF-8 -*-
from django.conf.urls.static import static

from . import views
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('all', views.list_view),
    path('add', views.add_view),
    path('updata/<int:note_id>', views.updata_note),
    path('delete', views.delete_note),
    path('make_page_csv', views.make_page_csv),
    path('upload', views.upload),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
