from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='index'),#call the def after go to the url '' to give show the response
    path('users/login', views.login_view, name='login'),
    path('users/singup', views.singup, name='singup'),
    path('users/logout', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
]
