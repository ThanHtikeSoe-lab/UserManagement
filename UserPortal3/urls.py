from django.contrib import admin 
from django.urls import path 
from UserPortal3 import views

urlpatterns=[
    path('',views.index,name='index'),
    path('log_in/',views.user_login,name='login'),
    path('sign_up/',views.user_signup,name='signup'),
      path('log_out/', views.user_logout, name = 'logout'),
]