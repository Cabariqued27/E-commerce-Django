from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path('',views.index, name='index'),#call the def after go to the url '' to give show the response
    path('admin/', admin.site.urls),
]
