from django.conf.urls import url
from django.contrib import admin

from .views import (
    create_todo,
    todo_update,
    todo_delete,
)

urlpatterns = [
    url(r'^create_todo/$', create_todo, name='create_todo'),
    url(r'^edit/(?P<id>\d+)/$', todo_update, name='todo_update'),
    url(r'^delete/(?P<id>\d+)/$', todo_delete, name='todo_delete'),
]