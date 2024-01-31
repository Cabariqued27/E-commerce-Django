from django.urls import path
from .import views
app_name = 'cart'
#por esto uso url 'cart:add', url 'cart:remove' etc etc

urlpatterns = [
    path('',views.cart, name='cart'),
    path('add', views.add, name='add'),
    path('remove', views.remove, name='remove')
]