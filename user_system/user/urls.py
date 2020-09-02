from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task', views.taskhome, name='task-home'),    
    path('task/<str:pk>/', views.tododetail, name='task'),
    path('add-task',views.addtask,name="add-task"),
    path('task/<str:pk>/update',views.update, name='update'),
    path('task/<str:pk>/delete', views.delete, name='delete'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('about',views.about, name='about'),
]