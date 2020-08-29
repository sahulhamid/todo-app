from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.contrib import messages
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages
def index(request):
    return render(request, 'user/index.html')

@login_required()
def home(request):
    current_user = request.user
    todos = current_user.todo_set.all()
    form = TodoForm(request.POST)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            completed = form.cleaned_data['completed']
            form = current_user.todo_set.create(title=title, completed=completed)
            form.save()
            return redirect('home')

    return render(request,'user/home.html', {'todos':todos, 'form':form})

@login_required()
def update(request,pk):
    sel_task = Todo.objects.get(id=pk)
    form = TodoForm(instance=sel_task)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=sel_task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'user/update.html', {'form':form})

@login_required()
def delete(request,pk):
    del_task = Todo.objects.get(id=pk)
    if request.method == 'POST':
        del_task.delete()
        return redirect('home')
    return render(request,'user/delete.html')

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            hashed_password = make_password(password)
            confirm_password = request.POST.get("confirm_password")

            if password != confirm_password:
                wrong='Wrong password'
                return render(request,'user/register.html',{'form':form,'wrong':wrong})
            user = User(username=username, password=hashed_password)
            user.save()
            return redirect('login')

    return render(request, 'user/register.html', {'form':form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('home')
    return render(request, 'user/login.html'  , {'form':form})

def logout(request):
    auth.logout(request)
    return render(request,'user/logout.html')


# @login_required()
# def addtask(request):
#     form=TodoForm()
#     if request.method=='POST':
#         form=TodoForm(request.POST)
#         if form.is_valid():
#             print('hello')
#             form.save()
#             return redirect('home')
#         else:
#             print('failed')    
#     context={'form':form}
#     return render(request,'user/add-task.html',context)    

def addtask(request):
    form=TodoForm()
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'user/add-task.html',context)

def about(request):
    return render(request,'user/about.html') 