from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User


class Status(models.Model):
    name_status = models.CharField(max_length=120)

    def __str__(self):
        return str(self.name_status)

    def __unicode__(self):
        return str(self.name_status)


class TodoList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)  # ,on_delete=models.CASCADE)
    name_list = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return str(self.name_list)

    def __unicode__(self):
        return str(self.name_list)

    def get_absolute_url(self):
        return "list/%s/" % (self.id)

    def get_delete_url(self):
        return reverse("delete_list", kwargs={"id": self.id})
        #return "todo/delete/%s/" % (self.id)

    def get_edit_url(self):
        return reverse("update_list", kwargs={"id": self.id})
        #return "todo/edit/%s/" % (self.id)


class Action(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True) # ,on_delete=models.CASCADE)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    action_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    action_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, blank=True, null=True)
    what_todo = models.CharField(max_length=300)
    # publish = models.DateField(auto_now=False, auto_now_add=False)
    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    execution_date = models.DateField()
    mini_list = models.TextField(blank=True, null=True)


    def __unicode__(self):
        return self.what_todo

    def __str__(self):
        return self.what_todo

    def get_delete_url(self):
        return reverse("todo:todo_delete", kwargs={"id": self.id})
        #return "todo/delete/%s/" % (self.id)

    def get_edit_url(self):
        return reverse("todo:todo_update", kwargs={"id": self.id})
        #return "todo/edit/%s/" % (self.id)





