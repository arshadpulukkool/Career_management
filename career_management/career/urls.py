from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home),
    path('register', views.register),
    path('login', views.loginform),
    path('adminhp', views.adminhome),
    path('home', views.homepage),
    path('home/addcourse', views.addcourse),
    path('home/showcourse', views.searchcourse),
    path('home/searchresult', views.searchresult),
    path('home/allcourse', views.allcourses),
    path('admins', views.adminshow),
    path('delete/<int:id>', views.admindelete),
    path('adminadd', views.adminaddcourse),


    # reset password urls #
    path('password_reset/', auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),



]