from django import forms
from .models import Action, TodoList
import datetime
from django.forms.extras.widgets import SelectDateWidget


class TodoForm(forms.ModelForm):
    execution_date = forms.DateField(widget=SelectDateWidget, initial=datetime.date.today )
    #action_list = forms.ModelChoiceField(queryset=Action.objects.filter(user_id=user))
    #def __init__(self, *args, **kwargs):
    #form.fields["rate"].queryset =

    action_list = forms.ModelChoiceField(queryset=TodoList.objects.all())
    class Meta:
        model = Action

        fields = [
            # "user",
            "action_status",
            "action_list",
            "what_todo",
            "execution_date",
            "mini_list",
        ]
        exclude = ["user"]


class TodoListForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = [
            # "user",
            "name_list",
        ]
        exclude = ["user"]