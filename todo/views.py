from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect, Http404

# Create your views here.
from .models import Action, Status, TodoList
from .forms import TodoForm, TodoListForm
#CreateUserView
from django.views import View
from datetime import date
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login ,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})

# ~~~~~~~~~~~~~~~~~~~~~~~ Action - to do ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# create one task
def create_todo(request):
    current_user = request.user.id
    if not request.user.is_authenticated:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    form = TodoForm(request.POST or None, request.FILES or None)
    form.fields["action_list"].queryset = TodoList.objects.filter(user_id=current_user)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = User.objects.get(id=request.user.id)
        instance.save()
        messages.success(request, "Task was successfully created! ")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        "form": form,
    }
    return render(request, 'todo_form.html', context)


# edit task
def todo_update(request, id=None):
    task = get_object_or_404(Action, id=id)
    current_user = request.user.id
    author = task.user_id
    if author != current_user:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    form = TodoForm(request.POST or None, request.FILES or None, instance=task)
    form.fields["action_list"].queryset = TodoList.objects.filter(user_id =current_user)

    if form.is_valid():
        task = form.save(commit=False)
        task.save()
        messages.info(request, "Task was successfully updated! ")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        "task": task,
        "form": form,
    }
    return render(request, 'todo_form.html', context)


# delete task
def todo_delete(request, id=None):
    instance = get_object_or_404(Action, id=id)
    current_user = request.user.id
    author = instance.user_id
    if author != current_user:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    instance.delete()
    messages.warning(request, "Task was successfully deleted! ")
    #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect("/")


# ~~~~~~~~~~~~~~~~~~~~~~~ Action - LIST of to do ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# list with all to-do lists + tasks

def list_of_todo(request):
    all_todos = Action.objects.all()
    lists = TodoList.objects.all()
    without_list = Action.objects.filter(action_list_id=None)
    print without_list
    context = {
        'all_todos': all_todos,
        'lists': lists,
        'without_list': without_list,
    }
    return render(request, 'list_of_todo.html', context)


# detail view of one list+task
def detail_todo_list(request, action_list_id = None):
    current_user = request.user.id
    all_fields = Action.objects.filter(action_list_id=action_list_id).filter(user_id=current_user)
    title = TodoList.objects.get(id=action_list_id)
    context = {
        "title": title,
        "all_fields": all_fields,
    }
    return render(request, "detail_todo.html", context)


# create one task
def create_todo_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    form_create_list = TodoListForm(request.POST or None, request.FILES or None)
    if form_create_list.is_valid():
        instance = form_create_list.save(commit=False)
        instance.user = User.objects.get(id=request.user.id)
        instance.save()
        messages.success(request, "Successfully created new list! ")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        "form": form_create_list,
    }
    return render(request, 'todo_form.html', context)


# edit list
def update_todo_list(request, id=None):
    task = get_object_or_404(TodoList, id=id)
    current_user = request.user.id
    author = task.user_id

    if author != current_user:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    form = TodoListForm(request.POST or None, request.FILES or None, instance=task)
    if form.is_valid():
        task = form.save(commit=False)
        task.save()
        messages.info(request, "Successfully updated list! ")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        #return HttpResponseRedirect("")
    context = {
        "task": task,
        "form": form,
    }
    return render(request, 'todo_form.html', context)


# delete list
def delete_todo_list(request, id=None):
    instance = get_object_or_404(TodoList, id=id)
    current_user = request.user.id
    author = instance.user_id
    if author != current_user:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    instance.delete()
    messages.warning(request, "Successfully deleted list!")
    return HttpResponseRedirect("/")


def register_user(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "User is Successfully created ")
        return HttpResponseRedirect('/')
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)


def authenticate_user(request):
    auth_form = AuthenticationForm(None, request.POST or None)
    if auth_form.is_valid():
        login(request, auth_form.get_user())
        print "auth_form.get_user()"
        print auth_form.get_user()
        print type(str(auth_form.get_user()))
        user_name = str(auth_form.get_user())
        messages.success(request, user_name + " is successfully loged in!")
        return HttpResponseRedirect("/")

    context = {
        "form": auth_form,
    }
    return render(request, 'login.html', context)


def logout_view(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        logout(request)
        messages.success(request, username + " is successfully loged out! ")
        return HttpResponseRedirect("/")
    else:
        messages.success(request, " You are not log in!  ")
    # Redirect to a success page.


def home_page(request):
    current_user = request.user.id
    lists = TodoList.objects.all().filter(user_id=current_user)
    today = date.today()
    list_today = Action.objects.filter(execution_date=today).filter(user_id=current_user)

    paginator = Paginator(list_today, 15)  # Show 25 contacts per page
    page = request.GET.get('page')
    page_request_var = "page"
    try:
        list_today = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list_today = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list_today = paginator.page(paginator.num_pages)
    context = {
        'today': today,
        'lists': lists,
        'list_today': list_today,
        'page_request_var': page_request_var,
    }
    return render(request, "home.html", context)
