from django.contrib import admin

# Register your models here.
from .models import Action, Status, TodoList


class ActionAdmin(admin.ModelAdmin):
    list_display = ('what_todo', 'timestamp', 'action_status','execution_date')

    # def get_queryset(self, request):
    #     qs = super(ActionAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(author=request.user)
    # def has_add_permission(self, request,obj = None):
    #     has_class_permission = super(ActionAdmin, self).has_add_permission(request)
    #     if not has_class_permission:
    #         return False
    #     if obj is not None and request.user.id != obj.added.id:
    #         return False
    #     return True
    #
    # def has_change_permission(self, request, obj=None):
    #
    # def has_delete_permission(self, request, obj=None):

admin.site.register(Status)
admin.site.register(TodoList)
admin.site.register(Action, ActionAdmin)
