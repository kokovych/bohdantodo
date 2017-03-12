"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls import  include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from todo.views import (
    home_page,
    list_of_todo,
    register_user,
    authenticate_user,
    logout_view,
    detail_todo_list,
    create_todo_list,
    update_todo_list,
    delete_todo_list,
    about,
    contact,

)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^list/$', list_of_todo, name='list_of_todo'),
    url(r'^todo/', include("todo.urls", namespace='todo')),
    url(r'^register/$',register_user , name='register'),
    url(r'^login/$',authenticate_user , name='login'),
    url(r'^logout/$',logout_view , name='logout'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^list/(?P<action_list_id>\d+)/$', detail_todo_list, name='detail_todo_list'),
    url(r'^create_list/$', create_todo_list, name='create_list'),
    url(r'^edit_list/(?P<id>\d+)/$', update_todo_list, name='update_list'),
    url(r'^delete_list/(?P<id>\d+)/$', delete_todo_list, name='delete_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)