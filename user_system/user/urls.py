from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-task',views.addtask,name="add-task"),
    path('update/<str:pk>/',views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('about',views.about, name='about'),
]