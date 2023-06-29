from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.startapp,name='start'),
    path('ad/register/', views.adminregisterPage, name='admin register'),
    path('newad/login/', views.adminLogInPage, name='New Admin Login'),
    path('newAdmin/', views.newAdminPage, name='New Admin Page'),
    path('user/', views.newUserPage, name='user'),
    path('login/', views.UserlogInPage, name='login'),
    path('logout/', views.logOutPage, name='logout'),
    path('register/', views.UserregisterPage, name='register'),
    path('user/api/appInfo/', views.appInfo.as_view()),
    path('task/api/tpInfo/', views.tpInfo.as_view()),
    path('points/api/tpInfo/', views.tpInfo.as_view()),
    path('task/', views.taskPage, name='task table'),
    path('points/',views.pointsPage,name='points table'),
    path('profile/',views.profilePage,name='profile'), 
    
]

# path('test',views.uploadin,name='uploading'),